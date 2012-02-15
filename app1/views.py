from django.contrib.auth import SESSION_KEY
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from app1.forms import CreateUserForm

@login_required(login_url='/login')
def home(request):

    return render_to_response('home.html', {'user':User.objects.get(pk=request.session[SESSION_KEY]),},context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateUserForm()

    return render_to_response('register.html', {'form':form,}, context_instance=RequestContext(request))