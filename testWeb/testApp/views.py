# Create your views here.
from datetime import date
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from testApp.models import Pastie

def index(request):
    last_pasties = Pastie.objects.all()[:5]
    context = { 'pasties': last_pasties }
    return render(request, 'testApp/index.html', context)

def paste(request):
    text = request.POST['text']
    p = Pastie(text=text, time_stamp=date.today())
    p.save() 

    return render(request, 'testApp/pastie/' + str(p.id), {})

def pastie(request, pastie_id):
    pastie = Pastie.objects.get(id=int(pastie_id))
    context = {'pastie' : pastie }
    
    return render(request, 'testApp/pastie.html', context)