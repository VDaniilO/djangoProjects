from django.shortcuts import render
from django.http import HttpResponse

from .models import logInf, Regions
# Create your views here.

def adminUsr(request):
    usr = logInf.objects.all()#requst for get all inf usr in my logInf db
    reg = Regions.objects.all()#requst for get all inf usr in my Regions db
    res = '<h1>List users</h1>'

    context = {
        'title': 'List users',
        'usersInf': usr,
        'regionInf': reg,
    }

    return render(request, template_name = 'mainPage/expPage.html', context = context)

def profileUsr(requst, usrInfo):
    usrLog = logInf.objects.filter(login = usrInfo)
    context = {
        'usrLog': usrLog,
    }
    return render(requst, template_name = 'mainPage/profilePage.html', context = context)
