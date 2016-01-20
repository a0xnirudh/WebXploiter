import re
import urllib2
import requests
from termcolor import colored

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Sql_injection():
    def __init__(self):
        pass

    def execute_all_func(self, target):
        self.check_cookies(target)
        self.check_user_agent(target)
        return

    def check_cookies(self, target):
        session = requests.Session()
        req = session.get(target)
        payload = open('Fuzzdatabase/error_sql.txt', 'r')
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

    def check_user_agent(self, target):
        payload = open('Fuzzdatabase/error_sql.txt', 'r')
        for i in payload.readlines():
            user_agent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'}
            user_agent['User-agent'] += i
            req = urllib2.Request(target, headers=user_agent)
            flag = str(urllib2.urlopen(req).read())
            check = ["MySQL server version", "have an error", "SQL syntax"]
            for j in range(0, len(check)):
                for line in re.finditer(check[j], flag):
                    print "======================================================="
                    print "Possible Attack: \n"
                    print "Error Based SQL Injection (User-Agent)"
                    print colored("POC: " + user_agent['User-agent'], "red")
                    print "Refer: http://resources.infosecinstitute.com/sql-injection-http-headers/ \n"
                    return
