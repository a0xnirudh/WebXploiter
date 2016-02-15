import sys
import os
import re
import requests

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '..')))

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'

from Modules.loggingManager.logging_manager import LoggingManager


class Others():
    # def __init__(self):

    def execute_all_func(self, target):
        self.logger = LoggingManager()
        self.websocket_tester(target)

    def websocket_tester(self, target):
        try:
            req = requests.get(target)
            check = ["ws://", "wss://", "WebSocket"]
            flag = str(req.text.encode('ascii', 'ignore'))
        except:
            print("Error while testing websockets. Check recon log for details\
                  .")
            self.logger.recon_log(e)
        for i in range(0, len(check)):
            for line in re.finditer(check[i], flag):
                print("=======================================================")
                print("Possible Attack: \n")
                print("Cross-Site WebSocket Hijacking (CSWSH)")
                print("Might be handy:  http://ironwasp.org/cswsh.html")
                return
