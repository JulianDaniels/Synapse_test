from django.shortcuts import render
from django.http import HttpResponse
from research.models import Bio
from django.template import context, loader

def index (request):
    return render(request, 'research/research.html')
def indexH (request):
    research_bio = Bio.objects.all()
    #t = loader.get_template('research/research.html')
    #c = context({'research_bio': research_bio,})
    return HttpResponse (research_bio)
    #return HttpResponse (t.render(c))
