from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from models import *

urlpatterns = patterns('sitio.views',
			url(r'^$', ListView.as_view(model=Videos,
										template_name="videos/video_list.html"
										),name="lista-videos"),
			url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(model=Videos,
														   template_name="videos/video_detail.html"
														   ),name="detalle-videos"),
			
                

    )