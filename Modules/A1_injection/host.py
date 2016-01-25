import os
import sys
import requests
from requests.exceptions import SSLError, ConnectionError
"""For appending the directory path"""
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '../..')))
from Print.printer import Print
from Modules.loggingManager.logging_manager import LoggingManager
__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Host_injection():
    def __init__(self):
        self.logger = LoggingManager()
        self.Print = Print()

    def host_header_inj(self, target):
        headers = {'Host': 'www.google.com'}
        header = {'X-Forwarded-Host': 'www.google.com'}
        check_host = "google.com"
        try:
            req = requests.get(target, headers=headers, allow_redirects=False)
            if req.status_code == 302 or req.status_code == 301:
                location = req.headers['Location']
                if check_host in location:
                    self.Print.printer(1, "Host Header injection",
                                       target, req.status_code)

            req = requests.get(target, headers=header, allow_redirects=False)
            if req.status_code == 302 or req.status_code == 301:
                location = req.headers['Location']
                if check_host in location:
                    self.Print.printer(1, "Host Header injection",
                                       target, req.status_code)

        except SSLError as e:
            self.Print.printer(1, "Host Header injection: Manual check needed",
                               target, req.status_code)

        except ConnectionError:
            self.Print.printer(1, "Host Header injection: ConnectionError",
                               target, req.status_code)

        except Exception as e:
            self.logger.error_log(e)
            print("Error occured while checking host header injection. Check
                  error log for details")
