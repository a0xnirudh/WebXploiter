import re
import requests
from termcolor import colored

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Attack():
    def __init__(self):
        pass

    def check_cookies(self, target):
        session = requests.Session()
        req = session.get(target)
        payload = open('fuzzdatabase/error_sql.txt', 'r')
        check = ["MySQL server version", "have an error", "SQL syntax"]
        for i in payload.readlines():
            i = i.strip("\n")
            for cookie in session.cookies:
                cookie.value += i
                r = session.get(target)
                for j in range(0, len(check)):
                    if check[j] in r.text:
                        print "======================================================="
                        print "Possible Attack: \n"
                        print colored("POC: " + cookie.name + ": " + cookie.value, "red")
                        print "Error Based SQL Injection (Cookie Based)"
                        print "Refer: https://www.exploit-db.com/docs/33253.pdf \n"
                        return
                # cookie = session.cookies
