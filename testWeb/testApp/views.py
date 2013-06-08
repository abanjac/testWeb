# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

from testApp.models import Pastie

def index(request):
    template = loader.get_template('testApp/index.html')
    context = Context({
        'text': "Hello world!",
    })
    return HttpResponse(template.render(context))

def pastie(request, pastie_id):

    pastie = Pastie.objects.get(id=int(pastie_id))
    template = loader.get_template('testApp/pastie.html')
    context = Context({
        'pastie' : pastie
    })
    
    return HttpResponse(template.render(context))