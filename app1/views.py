from django.contrib.auth import SESSION_KEY
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from app1.forms import CreateUserForm, AddTopic, AddDiscuss
from app1 import mongodb,forms

@login_required(login_url='/login')
def home(request):
    user = User.objects.get(pk=request.session[SESSION_KEY])
    topics = mongodb.getTwentyRandomTopics()

    return render_to_response('home.html', {'user':user, 'topics':topics},
        context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateUserForm()

    return render_to_response('register.html', {'form':form,}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def addtopic(request):
    if request.method == 'POST':
        form = AddTopic(request.POST)

        if form.is_valid():
            form.save(request.session[SESSION_KEY])
            return HttpResponseRedirect('/')

    else:
        form = AddTopic()

    return render_to_response('addtopic.html', {'form':form,}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def adddiscuss(request):
    if request.method == 'POST':
        form = AddDiscuss(request.POST)

        if form.is_valid():
            form.save(request.session[SESSION_KEY])
            return
    else:
        raise Http404