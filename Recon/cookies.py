import os
import sys
import base64
import binascii
import requests
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '..')))
from Print.printer import Print
from Modules.loggingManager.logging_manager import LoggingManager
__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Cookies():
    """ """
    def __init__(self):
        self.cookies = ""
        self.Print = Print()
        self.logger = LoggingManager()

    def execute_all_func(self, target):
        self.get_cookies(target)
        self.base64_check(target)

    def get_cookies(self, target):
        data = ""
        try:
            req = requests.get(target)
            self.cookies = req.cookies.items()
        except Exception as e:
            print("Error occured while accessing cookies. Check error log")
            self.logger.error_log(e)
        for name, value in self.cookies:
            length = len(name)
            length = 25 - length
            data = data + name + ": ".rjust(length) + value
        self.Print.printer(1, "Cookies: ", data)

    def base64_check(self, target):
        for name, value in self.cookies:
            try:
                flag = base64.decodestring(value.replace("%3D", "="))
                length = len(name)
                length = 25 - length
                data = name + ": ".rjust(length) + flag
                self.Print.printer(1, "Base64 Encoded Cookies: (Attention!)", data)
            except binascii.Error as e:
                continue
