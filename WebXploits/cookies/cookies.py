import requests

__author__ = 'Anirudh Anand (a0xnirudh)'


class Cookies():
    """ """
#    def __init__(self):
    def get_cookies(self, target):
        req = requests.get(target)
        cookies = req.cookies.items()
        print "==============================================================="
        print "Cookies: \n"
        for name, value in cookies:
            length = len(name)
            length = 25 - length
            print name + ": ".rjust(length) + value
