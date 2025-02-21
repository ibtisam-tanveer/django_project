from django.shortcuts import render
from django.http import HttpResponse

from asiatouragency.models import Tour
# Create your views here.

def index(req):
    tours = Tour.objects.all()
    context= {'tours':tours}
    return render(req,'tours/index.html',context)