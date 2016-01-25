import os
import sys
import requests
from contextlib import closing
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '..')))
from Print.printer import Print
__author__ = "AnirudhAnand <anirudh.anand@owasp.org>"


class Info_disclosure:
    def __init__(self):
        self.Print = Print()

    def check(self, target):
        req = requests.get(target+"/robots.txt")
        if req.status_code != 404:
            with closing(requests.get(target+"/robots.txt")) as stream:
                data = stream.text
                self.Print.printer(1, "Robots.txt analysis: ", data,
                                   req.status_code)

        req = requests.get(target+"/server-status")
        if req.status_code != 404:
            with closing(requests.get(target+"/server-status")) as stream:
                data = stream.text
            self.Print.printer(1, "server-status analysis: ", data,
                               req.status_code)

        req = requests.get(target+"/.svn/entries")
        if req.status_code != 404:
            with closing(requests.get(target+"/.svn/entries")) as stream:
                data = stream.text
            self.Print.printer(1, "Svn entries analysis: ", data,
                               req.status_code)

        req = requests.get(target+"/.htaccess")
        if req.status_code != 404:
            with closing(requests.get(target+"/.htaccess")) as stream:
                data = stream.text
            self.Print.printer(1, ".htaccess analysis: ", data,
                               req.status_code)
