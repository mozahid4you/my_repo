from django.shortcuts import render
from .models import Travellomodel

# Create your views here.
def travello(request):
    tra=Travellomodel.objects.all().order_by('-id')
    return render(request,'travello/index.html',{'travello':tra})
