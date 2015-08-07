import re
import requests


__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class Others():
    # def __init__(self):

    def execute_all_func(self, target):
        self.websocket_tester(target)

    def websocket_tester(self, target):
        req = requests.get(target)
        check = ["ws://", "wss://", "WebSocket"]
        flag = str(req.text.encode('ascii', 'ignore'))
        for i in range(0, len(check)):
            for line in re.finditer(check[i], flag):
                print "======================================================="
                print "Possible Attack: \n"
                print "Cross-Site WebSocket Hijacking (CSWSH)"
                print "Might be handy:  http://ironwasp.org/cswsh.html"
