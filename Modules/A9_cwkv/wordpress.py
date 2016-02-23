import os
import sys
import requests
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '../..')))
from Print.printer import Print
from Modules.loggingManager.logging_manager import LoggingManager
__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Wordpress():
    def __init__(self):
        self.logger = LoggingManager()
        self.Print = Print()

    def execute_all_func(self, target):
        self.info_disclosure(target)

    def info_disclosure(self, target):
        # User Enumeration
        authors_list = []
        flag = 1
        while True:
            url = target + "?author=" + str(flag)
            print(url)
            flag = flag + 1
            req = requests.get(url, allow_redirects=False)
            try:
                location = req.headers['location']
            except:
                location = ""
                pass
            if "author/" in location:
                # Getting the author name from HTTP header location
                author = req.headers['location'].split('author/')[1].strip('/')
                authors_list.append(author)
            else:
                print("Wordpress Users Enumerated \n")
                for i in authors_list:
                    print(i)
                break
