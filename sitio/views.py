from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sitio.models import *
import datetime
# Create your views here.

def index(request):
	''' vista del base del sitio
	'''
	#sabado son todos las charlas del sabado
	sabado = Videos.objects.filter(categoria=1).order_by('-fecha')[:1]
	#domingo es la variable que contiene el proximo taller
	domingo = Videos.objects.filter(categoria=2,proximo=True)
	#pasados son los videos pasadas de los talleres
	pasados = Videos.objects.filter(categoria=2).exclude(proximo=True).order_by('fecha')[:4]
	#primervideo es al ultimo taller impartido
	primervideo = Videos.objects.filter(categoria=2).order_by('fecha')[:1]

	#fecha para el conteo regresivo del proximo taller
	fecha_2 = [nose.fecha for nose in domingo][0]
	

	return render_to_response('base.html', locals(),
							   context_instance=RequestContext(request))


def detalle(request, slug):
	domingo = Videos.objects.filter(categoria=2,proximo=True).order_by('-fecha')
	video = get_object_or_404(Videos, slug=slug)

	return render_to_response('videos/video_detail.html', locals(),
							   context_instance=RequestContext(request))