import re
from django.contrib.auth import SESSION_KEY
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from djangoproj1.app1.forms import CreateUserForm, AddDiscuss
from djangoproj1.app1 import mongodb

@login_required(login_url='/login')
def home(request):
    user = User.objects.get(pk=request.session[SESSION_KEY])
    topics = mongodb.getTwentyRandomTopics()
    composedTopics = [topic for topic in topics]
    for topic in composedTopics:
        topic['topicId'] = topic['_id']
        topic['username'] = User.objects.get(pk=topic['userId']).username
        if 'topicTags' in topic:
            topicTags = topic['topicTags']
            topic['topicTags'] = re.split('[\s,;]+', topicTags)

    return render_to_response('home.html', {'user':user, 'topics':composedTopics,},
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
#    if request.method == 'POST':
##        form = AddTopic(request.POST)
##
##        if form.is_valid():
##            form.save(request.session[SESSION_KEY])
##            return HttpResponseRedirect('/')
#        pass
#    else:


    return render_to_response('addtopic.html', context_instance=RequestContext(request))

@login_required(login_url='/login')
def adddiscuss(request):
    if request.method == 'POST':
        form = AddDiscuss(request.POST)

        if form.is_valid():
            discussId = form.save(request.session[SESSION_KEY])
            newlyAddedDiscuss = mongodb.getSpecificDiscuss(discussId)
            newlyAddedDiscuss['username'] = User.objects.get(pk=newlyAddedDiscuss['userId']).username
            return render_to_response('discusscell.html', {'discuss':newlyAddedDiscuss,}, context_instance=RequestContext(request))
    else:
        raise Http404

def gettopic(request, topicId):
    topic = mongodb.getTopic(topicId)
    discusses = [discuss for discuss in mongodb.getDiscussOfaTopic(topicId) ]
    formInitialData = {'topicId': topicId}
    form = AddDiscuss(auto_id='id_adddiscuss_%s', initial=formInitialData)

    topic['username'] = User.objects.get(pk=topic['userId']).username
    for discuss in discusses:
        discuss['username'] = User.objects.get(pk=discuss['userId']).username

    return render_to_response('displaytopic.html', {'topic':topic, "discusses":discusses, 'adddiscussform':form},
        context_instance=RequestContext(request))