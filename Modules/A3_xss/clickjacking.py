import os
import logging
import requests
from ghost import Ghost
from termcolor import colored


class Clickjacking():
    def __init__(self):
        pass

    def check_protection(self, target):
        req = requests.get(target)
        try:
            xframe = req.headers['x-frame-options']
            print '\nX-FRAME-OPTIONS:', xframe, ' - Clickjacking not possible'
        except:
            print "\n======================================================="
            print "Possible Attack: \n"
            print "ClickJacking: \n"
            print colored('X-FRAME-OPTIONS is missing !', 'red')
            self.break_protection(target)

    def break_protection(self, target):
        print '\nAttempting ClickJacking... \n'
        html = '''
        <html>
        <body>
        <iframe src="'''+target+'''" height='600px' width='800px'></iframe>
        </body>
        </html>'''
        html_filename = 'clickjack.html'
        f = open(html_filename, 'w+')
        f.write(html)
        f.close()
        log_filename = 'test.log'
        fh = logging.FileHandler(log_filename)
        ghost = Ghost(log_level=logging.INFO, log_handler=fh)
        with ghost.start() as session:
            session.wait_timeout = 50
            page, resources = session.open(html_filename)
            l = open(log_filename, 'r')
            if 'forbidden by X-Frame-Options.' in l.read():
                print 'Clickjacking mitigated via X-FRAME-OPTIONS'
            else:
                href = session.evaluate('document.location.href')[0]
            if html_filename not in href:
                print 'Frame busting detected'
            else:
                print colored('Frame busting not detected, page is likely ' +
                              'vulnerable to ClickJacking', 'red')
            l.close()
            logging.getLogger('ghost').handlers[0].close()
            os.unlink(log_filename)
            os.unlink(html_filename)
