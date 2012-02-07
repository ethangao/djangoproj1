from django.http import HttpResponse

# Create your views here.
def home(request, year='2012'):
    return HttpResponse('hello world' + year)