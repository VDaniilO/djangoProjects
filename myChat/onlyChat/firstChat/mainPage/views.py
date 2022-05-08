from django.shortcuts import render, get_object_or_404

from .models import logInf, Regions
# Create your views here.

def adminUsr(request):
    usr = logInf.objects.all()#requst for get all inf usr in my logInf db
    res = '<h1>List users</h1>'

    context = {
        'title': 'List users',
        'usersInf': usr,
    }

    return render(request, template_name = 'mainPage/expPage.html', context = context)

def profileUsr(requst, usrInfo):
    #usrLog = logInf.objects.get(login = usrInfo)
    usrLog = get_object_or_404(logInf, login = usrInfo)
    context = {
        'usrLog': usrLog,
    }
    return render(requst, template_name = 'mainPage/profilePage.html', context = context)

def regionUsrFilter(requst, region_id):
    usr_reg = logInf.objects.filter(region = region_id)
    context = {
        'usrReg': usr_reg,
    }
    return render(requst, template_name = 'mainPage/regionUsr.html', context = context)
