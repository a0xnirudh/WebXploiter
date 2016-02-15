import os
import re
import sys
import urllib.request
import requests
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '../..')))
from Print.printer import Print
from Modules.loggingManager.logging_manager import LoggingManager

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Sql_injection():
    def __init__(self):
        self.Print = Print()
        self.logger = LoggingManager()
        self.filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '../..'))

    def execute_all_func(self, target):
        try:
            self.check_cookies(target)
        except Exception as e:
            print("Error while checking cookies.Check module log for details")
            self.logger.module_log(e)
        try:
            self.check_user_agent(target)
        except Exception as e:
            print("Error while checking user agent.Check module log for details.")
            self.logger.module_log(e)
        return

    def check_cookies(self, target):
        session = requests.Session()
        req = session.get(target)
        payload = open(self.filepath + '/Fuzzdatabase/error_sql.txt', 'r')
        check = ["MySQL server version", "have an error", "SQL syntax"]
        for i in payload.readlines():
            i = i.strip("\n")
            for cookie in session.cookies:
                cookie.value += i
                r = session.get(target)
                for j in range(0, len(check)):
                    if check[j] in r.text:
                        poc = "POC: " + cookie.name + ": " + cookie.value
                        self.Print.printer(3, "Error Based SQLi(Cookie Based)",
                                           None, req.status_code, poc)
                        return

    def check_user_agent(self, target):
        payload = open(self.filepath + '/Fuzzdatabase/error_sql.txt', 'r')
        for i in payload.readlines():
            user_agent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux' +
                          'x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'}
            user_agent['User-agent'] += i
            req = urllib.request.Request(target, headers=user_agent)
            flag = str(urllib.request.urlopen(req).read())
            check = ["MySQL server version", "have an error", "SQL syntax"]
            for j in range(0, len(check)):
                for line in re.finditer(check[j], flag):
                    self.Print.printer(3, "Error Based SQLi(User Agent)",
                                       None, None,None)
                    return
