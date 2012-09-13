from django.shortcuts import render_to_response
from django.template import RequestContext
from sitio.models import *
import datetime
# Create your views here.

def index(request):

	sabado = Videos.objects.filter(categoria=1).order_by('-fecha')[:1]
	domingo = Videos.objects.filter(categoria=2,proximo=True).order_by('-fecha')
	lista = []
	for curso in Cursos.objects.all():
		lista.append(Videos.objects.filter(curso=curso))

	#calculo de los dias que faltan para el proximo taller
	fecha_1 = datetime.date.today()
	fecha_2 = [nose.fecha for nose in domingo][0]
	fecha_final = fecha_2 - fecha_1
	horas = datetime.datetime.today().time().__str__().split('.')[0] 	
	nose = ('%s:%s') % (fecha_final.days,horas)
	#------------------------------------------------------
	fecha_actual = nose

	return render_to_response('base.html', locals(),
							   context_instance=RequestContext(request))