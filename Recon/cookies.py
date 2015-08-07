import base64
import binascii
import requests
from termcolor import colored
__author__ = 'Anirudh Anand (a0xnirudh)'


class Cookies():
    """ """
    def __init__(self):
        self.cookies = ""

    def execute_all_func(self, target):
        self.get_cookies(target)
        self.base64_check(target)

    def get_cookies(self, target):
        req = requests.get(target)
        self.cookies = req.cookies.items()
        print "==============================================================="
        print "Cookies: \n"
        for name, value in self.cookies:
            length = len(name)
            length = 25 - length
            print name + ": ".rjust(length) + value

    def base64_check(self, target):
        for name, value in self.cookies:
            try:
                flag = base64.decodestring(value.replace("%3D", "="))
                length = len(name)
                length = 25 - length
                print colored("\nBase64 Encoded Cookies: (Attention!)", "red")
                print name + ": ".rjust(length) + flag

            except binascii.Error:
                continue
