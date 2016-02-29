from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
import os
import sys
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abs_path+'/../../../')
from Print.printer import Print
from WebXploiter import WebXploit


def index(request):
        webxploit = WebXploit()
        webxploit.recon_others.execute_all_func("http://127.0.0.1/challenge.php")
        webxploit.sql.execute_all_func("http://127.0.0.1/challenge.php")
        webxploit.crlf.test_crlf_injection("http://127.0.0.1/challenge.php")
        webxploit.host.host_header_inj("http://127.0.0.1/challenge.php")
        vuln = {}
        vuln["Count"] = [0, 0, 0, 0]
        for _, data in Print.jsonData.items():
            (vuln["Count"])[int(data["Severity"])] += 1
        context = {
                'vuln': vuln,
        }
        Print.jsonData = {}
        return render(request, 'showData/index.html', context)
