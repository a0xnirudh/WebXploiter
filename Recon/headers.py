import os
import sys
import requests
from urlparse import urlparse
from contextlib import closing
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Print.printer import Print
__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Headers():
    def __init__(self):
        self.target_url = ""
        self.target_host = ""
        self.target_port = ""
        self.Print = Print()

    def execute_all_func(self, target):
        self.parse_target(target)
        self.get_headers(target)
        self.get_robots_txt(target)
        self.check_headers(target)

    def parse_target(self, target):
        self.target_url = target
        flag = urlparse(target)
        self.target_host = flag.scheme + "://" + flag.netloc
        self.target_port = flag.port

    def get_headers(self, target):
        data = ""
        req = requests.head(self.target_url)
        for name, value in req.headers.items():
            length = len(name)
            length = 50 - length
            data = data + name + ": ".rjust(length) + value + "\n"
        self.Print.printer(1, "Response Headers: ", data)

    def get_robots_txt(self, target):
        with closing(requests.get(self.target_host+"/robots.txt")) as stream:
            data = stream.text
        self.Print.printer(1, "Robots.txt Analysis: ", data)
        with closing(requests.get(self.target_host+"/.htaccess")) as stream:
            data = stream.text
        self.Print.printer(1, ".htaccess Analysis: ", data)

    def check_headers(self, target):
        req = requests.head(self.target_url)
        print "\n"
        self.Print.printer(1, "Response header Analysis: ", None)
        try:
            xssprotect = req.headers['X-XSS-Protection']
            if xssprotect != '1; mode=block':
                self.Print.printer(0, "X-XSS-Protection not set properly, XSS may be possible:", xssprotect)
        except:
                self.Print.printer(0, "X-XSS-Protection not set, XSS may be possible", None)
        try:
            contenttype = req.headers['X-Content-Type-Options']
            if contenttype != 'nosniff':
                self.Print.printer(0, "X-Content-Type-Options not set properly:", contenttype)
        except:
            self.Print.printer(0, "X-Content-Type-Options not set", None)
        try:
            hsts = req.headers['Strict-Transport-Security']
        except:
            self.Print.printer(0, "HSTS header not set, MITM attacks may be possible", None)
        try:
            csp = req.headers['Content-Security-Policy']
            self.Print.printer(0, "Content-Security-Policy set: ", csp)
        except:
            self.Print.printer(0, "Content-Security-Policy missing", None)
