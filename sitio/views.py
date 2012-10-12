from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sitio.models import *
import datetime
import GeoIP
import time
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
	pais = get_pais(request.META)
	print pais
	timestamp = get_timestamp()
	print timestamp

	return render_to_response('base.html', locals(),
							   context_instance=RequestContext(request))


def detalle(request, slug):
	domingo = Videos.objects.filter(categoria=2,proximo=True).order_by('-fecha')
	video = get_object_or_404(Videos, slug=slug)

	return render_to_response('videos/video_detail.html', locals(),
							   context_instance=RequestContext(request))

def domingo_taller(now):
    _4PM = datetime.time(hour=19)
    _JUE = 6  # Monday=0 for weekday()
    old_now = now
    now += datetime.timedelta((_JUE - now.weekday()) % 7)
    now = now.combine(now.date(), _4PM)
    if old_now >= now:
        now += datetime.timedelta(days=7)
    return now


def get_timestamp():
    now = datetime.datetime.now()
    sig_jueves = domingo_taller(now)
    return int(time.mktime(sig_jueves.timetuple()) * 1000)

def get_pais(meta):
    geo = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

    # por si el usuario esta detras de un proxy
    if 'HTTP_X_FORWARDED_FOR' in meta and meta['HTTP_X_FORWARDED_FOR']:
        ip = meta['HTTP_X_FORWARDED_FOR'].split(',')[0]
    else:
        ip = meta['REMOTE_ADDR']

    country = geo.country_name_by_addr(ip)
    if country is None:
        country = ''

    return country

def locateme(request):
    return HttpResponse(get_pais(request.META))