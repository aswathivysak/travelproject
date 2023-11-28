from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import place,Team
def index(request):
    obj=place.objects.all()
    tmobj=Team.objects.all()
    return render(request,'index.html',{'result':obj,'teamobj':tmobj})
