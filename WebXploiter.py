import os
import sys
import argparse
import requests
"""For appending the directory path"""
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abs_path+'/')

from Recon.cookies import Cookies
from Recon.headers import Headers
from Recon.others import Others
from Recon.httpmethods import HTTPMethods

from Modules.A1_injection.sql import Sql_injection
from Modules.A1_injection.crlf import Crlf_injection

from Modules.A3_xss.clickjacking import Clickjacking

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class WebXploit():
    """ """
    def __init__(self):
        self.recon_headers = Headers()
        self.recon_cookies = Cookies()
        self.recon_methods = HTTPMethods()
        self.recon_others = Others()

        self.sql = Sql_injection()
        self.crlf = Crlf_injection()

        self.clickjacking = Clickjacking()

    def launch(self):
        os.system("toilet -F metal WebXploit - Recon")

    def get_headers(self, target):
        self.recon_headers.execute_all_func(target)

    def get_cookies(self, target):
        self.recon_cookies.execute_all_func(target)

    def execute_random_vulns(self, target):
        self.recon_others.execute_all_func(target)

    def get_HTTP_methods(self, target):
        self.recon_methods.test_allowed_methods(target)


def main():
    webxpoit = WebXploit()

    parser = argparse.ArgumentParser(description=
                                     'Do a basic Recon for Web challenges')
    parser.add_argument('-u', '-url', type=str, help='Target URL to Recon')

    parser.add_argument('-a', '-all', help="Try all possible attacks",
                        action="store_true")
    parser.add_argument('-A1', help="Test for only Injection Attacks",
                        action="store_true")
    parser.add_argument('-A3', help="Test for only XSS Attacks",
                       action="store_true")

    args = parser.parse_args()

    if not args.u:
        print "No URL specified.\npython WebXploiter.py -h for help"
        exit(0)

    webxpoit.launch()
    webxpoit.get_headers(args.u)

    if args.A3:
        webxpoit.clickjacking.check_protection(args.u)

    webxpoit.get_cookies(args.u)
    webxpoit.get_HTTP_methods(args.u)

    if args.a:
        args.A1 = True
        args.A3 = True
        webxpoit.recon_others.execute_all_func(args.u)

    if args.A1:
        webxpoit.sql.execute_all_func(args.u)
        webxpoit.crlf.test_crlf_injection(args.u)

if __name__ == '__main__':
    main()
