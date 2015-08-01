import re
import urllib2
from termcolor import colored

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Attack():
    def __init__(self):
        pass

    def check_user_agent(self, target):
        payload = open('fuzzdatabase/error_sql.txt', 'r')
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
                    print colored("POC: " + user_agent['User-agent'], "red")
                    print "Error Based SQL Injection (User-Agent)"
                    print "Refer: http://resources.infosecinstitute.com/sql-injection-http-headers/ \n"
                    return
