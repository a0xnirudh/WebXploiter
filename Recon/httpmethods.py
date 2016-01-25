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
        self.logger = LoggingManager()
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
                self.logger.recon_log(e)
            except Exception as e:
                self.logger.recon_log(e)
                print("Error while testing allowed methords. Check recon log")
