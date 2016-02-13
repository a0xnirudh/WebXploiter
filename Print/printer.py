import json
import os
__author__ = 'a0xnirudh'


class Print():

    def __init__(self):
        pass

    def printer(self, main, name, data, status=None, poc=None):
	jsonData={}
        if main:
            print "\n========================================================="
        print name + "\n"
        if data:
            print "Analysis: \n" + data + "\n"
	    jsonData["Analysis"] = data
        if poc:
            print poc + "\n"
	    jsonData["POC"] = poc
        if status:
            print "Status code: " + str(status)
	    jsonData["Status"] = str(status)
	    fileObj = open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'../Logs/toDisplay'),'w')
	    fileObj.write(json.dumps(jsonData))	    
