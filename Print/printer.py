import json
import os
__author__ = 'a0xnirudh'


class Print():
    jsonData = {}
    count = 0

    def __init__(self):
        pass

    def printer(self, severity, name, data, status=None, poc=None):
        Print.count = Print.count + 1
        (Print.jsonData[Print.count]) = {}
        #print name + "\n"
        if severity!=None:
            #print "\n========================================================="
            #print("Severity : " + str(severity))
            (Print.jsonData[Print.count])['Severity'] = str(severity)
        if data:
            #print "Analysis: \n" + data + "\n"
            (Print.jsonData[Print.count])["Analysis"] = data
        if poc:
            #print poc + "\n"
            (Print.jsonData[Print.count])["POC"] = poc
            '''
        if status:
            print "Status code: " + str(status)
            jsonData["Status"] = str(status)
            '''
        if name:
            (Print.jsonData[Print.count])["Name"] = str(name)

    def writeFile(self):
        fileObj = open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'../Logs/toDisplay'),'a')
        fileObj.write(json.dumps(Print.jsonData))
        fileObj.write("\n")
