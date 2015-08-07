import re
import requests
from termcolor import colored

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Crlf_injection():
    def __init__(self):
        pass

    def test_crlf_injection(self, target):
        payload = open('fuzzdatabase/crlf_injection_fuzzer.txt', 'r')
        if (target[:-1].endswith('/')) == False:
            target += "/"
        flag = requests.get(target)
        for i in payload.readlines()[1:]:
            req = requests.get(target + i)
            if req.text == flag.text:
                continue
            status = req.status_code
            if status != 404 and status != 403 and status != 401 and status != 400:
                print "======================================================="
                print "Possible Attack: \n"
                print "CRLF header Injection"
                print colored("POC: " + target + i + " is giving statuscode:" +
                              str(req.status_code), "red")
        return
