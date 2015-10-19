import requests
from termcolor import colored


class HTTPMethods():

    def __init__(self):
        self.verbs = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE']

    def test_allowed_methods(self, target):
        print "\n==============================================================="
        print "HTTP Methods:"
        for verb in self.verbs:
            req = requests.request(verb, target)
            print verb, req.status_code, req.reason
            if verb == 'TRACE' and 'TRACE / HTTP' in req.text:
                print colored('Possible Cross Site Tracing vulnerability found', 'red')
