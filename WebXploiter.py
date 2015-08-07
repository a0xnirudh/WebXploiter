import os
import sys
import argparse
import requests
"""For appending the directory path"""
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abs_path+'/')

from rand.random import Random
from cookies.cookies import Cookies
from headers.headers import Headers

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class WebXploit():
    """ """
    def __init__(self):
        self.cookies = Cookies()
        self.headers = Headers()
        self.random = Random()

    def launch(self):
        os.system("toilet -F metal WebXploit - Recon")

    def get_headers(self, target):
        self.headers.execute_all_func(target)

    def get_cookies(self, target):
        self.cookies.execute_all_func(target)

    def execute_random_vulns(self, target):
        self.random.execute_all_func(target)


def main():
    webxpoit = WebXploit()

    parser = argparse.ArgumentParser(description=
                                     'Do a basic Recon for Web challenges')
    parser.add_argument('-u', '-url', type=str, help='Target URL to Recon')
    parser.add_argument('-o', '-out', type=str, help='Filename to save output')
    parser.add_argument('-a', '-all', help="Try all possible attacks",
                        action="store_true")
    parser.add_argument('-crlf', help="Testing for CRLF Injections",
                        action="store_true")
    args = parser.parse_args()

    if not args.u:
        print "No URL specified.\npython WebXploiter.py -h for help"
        exit(0)

    webxpoit.launch()
    webxpoit.get_headers(args.u)
    webxpoit.get_cookies(args.u)
    webxpoit.execute_random_vulns(args.u)

    if args.a:
        webxpoit.headers.header_injection(args.u)
        webxpoit.cookies.cookie_err_injection(args.u)
        webxpoit.headers.crlf_injection(args.u)

    if args.crlf:
        webxpoit.headers.crlf_injection(args.u)

if __name__ == '__main__':
    main()
