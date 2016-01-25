import os
import sys
import requests
from urlparse import urlparse
from contextlib import closing
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '..')))
from Print.printer import Print
from Modules.loggingManager.logging_manager import LoggingManager
__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Headers():
    def __init__(self):
        self.Print = Print()
        self.logger = LoggingManager()

    def execute_all_func(self, target):
        self.get_headers(target)
        self.check_headers(target)

    def get_headers(self, target):
        data = ""
        try:
            req = requests.head(target)
        except requests.exceptions.MissingSchema as e:
            print("Non valid URL. Please specify a valid URL.")
            self.logger.error_log(e)
            exit()
        except Exception as e:
            print("Error occured while accessing headers.Check error log")
            self.logger.error_log(e)
            exit()
        for name, value in req.headers.items():
            length = len(name)
            length = 50 - length
            data = data + name + ": ".rjust(length) + value + "\n"
        self.Print.printer(1, "Response Headers: ", data)

    def check_headers(self, target):
        req = requests.head(target)
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
