# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sitio.models import *
# Create your views here.

def index(request):
	''' vista del base del sitio
	'''
	tiempo = EnVivo.objects.filter(en_vivo=True).count()
	if tiempo:
		vivo = EnVivo.objects.filter(en_vivo=True)
		return render_to_response('vivo.html', locals(),
							      context_instance=RequestContext(request))
	#primer taller es la variable que contiene el proximo taller
	primervideo = Videos.objects.filter(categoria=2,portada=True)

	#pasados son los videos pasadas de los talleres
	pasados = Videos.objects.filter(categoria=2).exclude(portada=True).order_by('-fecha')[:4]

	return render_to_response('base.html', locals(),
							   context_instance=RequestContext(request))


def detalle(request, slug):
	''' funcion que devuelve el video seleccionado '''

	video = get_object_or_404(Videos, slug=slug)
	return render_to_response('videos/video_detail.html', locals(),
							   context_instance=RequestContext(request))

def comunidades(request):
	comus = ComunidadAmiga.objects.all()
	
	return render_to_response('comunidades.html', locals(),
						context_instance=RequestContext(request))

