from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import json

def index(request):
        fileObj = open("../../Logs/toDisplay",'r')
        data = json.loads(fileObj.read())
        context = {
                'latest_question_list':data,
        }
        return render(request,'showData/index.html',context)
