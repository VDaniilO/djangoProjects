from django.shortcuts import render
from django.http import HttpResponse

from .models import logInf, Regions
# Create your views here.

def adminUsr(request):
    usr = logInf.objects.all()#requst for get all inf usr in my db
    res = '<h1>List users</h1>'

    context = {
        'title': 'List users',
        'usersInf': usr,
    }

    return render(request, template_name = 'mainPage/expPage.html', context = context)
