import os
import sys
import requests
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '../..')))
from Print.printer import Print
from Modules.loggingManager.logging_manager import LoggingManager
__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Crlf_injection():
    def __init__(self):
        self.Print = Print()
        self.logger = LoggingManager()
        self.filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '../..'))

    def test_crlf_injection(self, target):
        payload = open(self.filepath + '/Fuzzdatabase/crlf_fuzzer.txt', 'r')
        if (target[:-1].endswith('/')) == False:
            target += "/"
        try:
            flag = requests.get(target)
            for i in payload.readlines()[1:]:
                req = requests.get(target + i)
                if req.text == flag.text:
                    continue
                    status = req.status_code
                    if status != 404 and status != 403 and status != 400:
                        poc = "POC: " + target + i
                        self.Print.printer(1, "CRLF header Injection",
                                           data, status, poc)
        except Exception as e:
            print("Error occured while checking for crlf injection. Check error\
                  log for details")
            self.logger.error_log(e)
        return
