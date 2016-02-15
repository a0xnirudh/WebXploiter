from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
import os
import sys
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abs_path+'/../../../')
from Print.printer import Print
from Modules.A1_injection.sql import Sql_injection


def index(request):
        #fileObj = open("../../Logs/toDisplay", 'r')
        sql = Sql_injection()
        sql.execute_all_func("http://127.0.0.1/challenge.php")
        vuln = {}
        vuln["Count"] = [0, 0, 0, 0]
        vuln["Target"] = (Print.jsonData[0])["Name"]
        for data in Print.jsonData[1:]:
            (vuln["Count"])[int(data["Severity"])] += 1
        context = {
                'vuln': vuln,
        }
        return render(request, 'showData/index.html', context)
