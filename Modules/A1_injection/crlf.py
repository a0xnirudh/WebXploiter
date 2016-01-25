import os
import sys
import requests
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '../..')))
from Print.printer import Print

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Crlf_injection():
    def __init__(self):
        self.Print = Print()
        self.filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '../..'))

    def test_crlf_injection(self, target):
        payload = open(self.filepath + '/Fuzzdatabase/crlf_injection_fuzzer.txt', 'r')
        if (target[:-1].endswith('/')) == False:
            target += "/"
        flag = requests.get(target)
        for i in payload.readlines()[1:]:
            req = requests.get(target + i)
            if req.text == flag.text:
                continue
            status = req.status_code
            if status != 404 and status != 403 and status != 401 and status != 400:
                print "CRLF header Injection"
                poc = "POC: " + target + i + " is giving statuscode:" + str(req.status_code)
        return
