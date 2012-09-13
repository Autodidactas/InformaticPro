from django.shortcuts import render_to_response
from django.template import RequestContext
from sitio.models import *
# Create your views here.

def index(request):

	sabado = Videos.objects.filter(categoria=1).order_by('-fecha')[:1]
	domingo = Videos.objects.filter(categoria=2,proximo=True).order_by('-fecha')
	lista = []
	for curso in Cursos.objects.all():
		lista.append(Videos.objects.filter(curso=curso))

	return render_to_response('base.html', locals(),
							   context_instance=RequestContext(request))