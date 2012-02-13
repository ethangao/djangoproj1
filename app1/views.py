from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render_to_response
from app1 import forms
from app1.forms import CreateUserForm

def home(request, year='2012'):

    return HttpResponse('hello world' + year)

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateUserForm()

    return render_to_response('register.html', {'form':form,})