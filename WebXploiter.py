import os
import sys
import argparse
import requests
from urllib.parse import urlparse
from Print.printer import Print
from Recon.cookies import Cookies
from Recon.headers import Headers
from Recon.others import Others
from Recon.httpmethods import HTTPMethods

from Modules.A1_injection.sql import Sql_injection
from Modules.A1_injection.crlf import Crlf_injection
from Modules.A1_injection.host import Host_injection


from Modules.A9_cwkv.wordpress import Wordpress
from Modules.A9_cwkv.apache import Apache2_tests

from Modules.loggingManager.logging_manager import LoggingManager
"""For appending the directory path"""
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abs_path+'/')

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'

logger = LoggingManager()


class WebXploit():
    def __init__(self):
        self.target_url = ""
        self.target_port = ""
        self.target_host = ""
        self.logger = logger
        self.recon_headers = Headers()
        self.recon_cookies = Cookies()
        self.recon_methods = HTTPMethods()
        self.recon_others = Others()

        self.sql = Sql_injection()
        self.crlf = Crlf_injection()
        self.host = Host_injection()


        self.apache = Apache2_tests()
        self.wordpress = Wordpress()

        self.Print = Print()

    def parse_target(self, target):
        try:
            self.target_url = target
            flag = urlparse(target)
            self.target_host = flag.scheme + "://" + flag.netloc
            print("Target"+str(self.target_host))
            self.target_port = flag.port
        except Exception as e:
            self.logger.error_log(e)
        self.Print.printer(None, self.target_url, None)

    def launch(self):
        os.system("toilet -F metal WebXploit - Recon")

    def get_headers(self, target):
        self.recon_headers.execute_all_func(self.target_url)

    def get_cookies(self, target):
        self.recon_cookies.execute_all_func(target)

    def execute_random_vulns(self, target):
        self.recon_others.execute_all_func(target)

    def get_HTTP_methods(self, target):
        self.recon_methods.test_allowed_methods(target)


def main():
    webxploit = WebXploit()

    parser = argparse.ArgumentParser(description=
                                     'Do a basic Recon for Web challenges')
    parser.add_argument('-u', '-url', type=str, help='Target URL to Recon')

    parser.add_argument('-a', '-all', help="Try all possible attacks",
                        action="store_true")
    parser.add_argument('-A1', help="Test for only Injection Attacks",
                        action="store_true")
    parser.add_argument('-A3', help="Test for only XSS Attacks",
                        action="store_true")
    parser.add_argument('-A9', help="Test for known software vulnerabilities",
                        action="store_true")
    parser.add_argument('-wordpress', help="Testing Wordpress vulnerabilities",
                        action="store_true")

    args = parser.parse_args()

    webxploit.parse_target(args.u)

    if not args.u:
        print("No URL specified.\npython WebXploiter.py -h for help")
        exit(0)

    webxploit.launch()
    webxploit.get_headers(args.u)
    webxploit.get_cookies(args.u)
    webxploit.get_HTTP_methods(args.u)

    if args.a:
        args.A1 = True
        args.A3 = True
        args.A9 = True
        webxploit.recon_others.execute_all_func(args.u)

    if args.A1:
        webxploit.sql.execute_all_func(args.u)
        webxploit.crlf.test_crlf_injection(args.u)
        webxploit.host.host_header_inj(args.u)

    if args.A9:
        webxploit.apache.execute_all_func(webxploit.target_host)

    if args.wordpress:
        webxploit.wordpress.execute_all_func(webxploit.target_host)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Unhandled error occured. Check error log for details")
        logger.error_log(e)
