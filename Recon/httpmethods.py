import os
import sys
import requests
from Print.printer import Print
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '..')))
__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'
from Modules.loggingManager.logging_manager import LoggingManager


class HTTPMethods():

    def __init__(self):
        self.Print = Print()
        self.verbs = ['GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE']

    def test_allowed_methods(self, target):
        for verb in self.verbs:
            try:
                req = requests.request(verb, target)
                print verb, req.status_code, req.reason
                if verb == 'TRACE' and 'TRACE / HTTP' in req.text:
                    print colored('Possible Cross Site Tracing vulnerability found', 'red')
            except requests.exceptions.ConnectionError as e:
                print("CONNECT :: Connection error occured. Retry using https")
                logger = LoggingManager()
                logger.error_log(e)
                #test = LoggingManager()
                #test2 = test.create_logger('test_log','test_log.log')
                #test2.exception(e)
