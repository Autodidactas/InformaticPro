from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sitio.models import *
import datetime
# Create your views here.

def index(request):

	sabado = Videos.objects.filter(categoria=1).order_by('-fecha')[:1]
	domingo = Videos.objects.filter(categoria=2,proximo=True).order_by('-fecha')
	pasados = Videos.objects.filter(categoria=2).order_by('-fecha')[:4]
	lista = []
	for curso in Cursos.objects.all():
		lista.append(Videos.objects.filter(curso=curso))

	#fecha para el conteo regresivo del proximo taller
	fecha_2 = [nose.fecha for nose in domingo][0]
	

	return render_to_response('base.html', locals(),
							   context_instance=RequestContext(request))


def detalle(request, slug):
	domingo = Videos.objects.filter(categoria=2,proximo=True).order_by('-fecha')
	video = get_object_or_404(Videos, slug=slug)

	return render_to_response('videos/video_detail.html', locals(),
							   context_instance=RequestContext(request))