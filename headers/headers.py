import requests
from urlparse import urlparse
from contextlib import closing

from attack import Attack
__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Headers(Attack):
    def __init__(self):
        self.attacks = Attack()
        self.target_url = ""
        self.target_host = ""
        self.target_port = ""

    def execute_all_func(self, target):
        self.parse_target(target)
        self.get_headers(target)
        self.get_robots_txt(target)

    def parse_target(self, target):
        self.target_url = target
        flag = urlparse(target)
        self.target_host = flag.scheme + "://" + flag.netloc
        self.target_port = flag.port

    def get_headers(self, target):
        req = requests.head(self.target_url)
        print "==============================================================="
        print "Response Headers: \n"
        for name, value in req.headers.items():
            length = len(name)
            length = 25 - length
            print name + ": ".rjust(length) + value

    def get_robots_txt(self, target):
        print "==============================================================="
        print "Robots.txt Analysis: \n"
        with closing(requests.get(self.target_host+"/robots.txt")) as stream:
            print stream.text

    def header_injection(self, target):
        self.attacks.check_user_agent(target)

    def crlf_injection(self, target):
        self.attacks.crlf_injection(target)
