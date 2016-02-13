from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import json

def index(request):
        fileObj = open("../../Logs/toDisplay",'r')
        vuln = [0, 0, 0, 0]
        for line in fileObj.readlines():
            data = json.loads(line)
            vuln[int(data["Severity"])] += 1
        #data = json.loads(fileObj.read())
        context = {
                'vuln':vuln,
        }
        return render(request,'showData/index.html',context)
