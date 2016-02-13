import json
import os
__author__ = 'a0xnirudh'


class Print():

    def __init__(self):
        pass

    def printer(self, severity, name, data, status=None, poc=None):
        jsonData = {}
        print name + "\n"
        if severity!=None:
            #print "\n========================================================="
            print("Severity : " + str(severity))
            jsonData['Severity'] = str(severity)
        if data:
            print "Analysis: \n" + data + "\n"
            jsonData["Analysis"] = data
        if poc:
            print poc + "\n"
            jsonData["POC"] = poc
            '''
        if status:
            print "Status code: " + str(status)
            jsonData["Status"] = str(status)
            ''' 
        if name:
            jsonData["Name"] = str(name)
        fileObj = open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'../Logs/toDisplay'),'a')
        fileObj.write(json.dumps(jsonData))
        fileObj.write("\n")
