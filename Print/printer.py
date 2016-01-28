__author__ = 'a0xnirudh'


class Print():

    def __init__(self):
        pass

    def printer(self, main, name, data, status=None, poc=None):
        if main:
            print "\n========================================================="
        print name + "\n"
        if data:
            print "Analysis: \n" + data + "\n"
        if poc:
            print poc + "\n"
        if status:
            print "Status code: " + str(status)
