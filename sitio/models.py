# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
import os

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
    	return self.nombre

    class Meta:
    	verbose_name_plural = "Categorias para los videos"

class Cursos(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Cursos para los videos"

class Redes(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "nombre de las redes sociales"

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	descripcion = models.TextField()

	def __unicode__(self):
		return u"%s - %s" % (self.user.username, self.descripcion)


class Social(models.Model):
	red = models.ForeignKey('Redes')
	url = models.CharField('urls', max_length=100)
	usuario = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return u"%s - %s" % (self.red.nombre, self.usuario.user.username)

	class Meta:
		verbose_name_plural = "Social"
		
class Videos(models.Model):
	titulo = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	fecha = models.DateTimeField()
	descripcion = models.TextField('Descripción')
	url = models.URLField()
	tags = TagAutocompleteField("Tags",help_text='Separar elementos con "," ', null=True, blank=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True)
	curso = models.ForeignKey(Cursos, null=True, blank=True)
	usuario = models.ForeignKey(User)
	portada = models.BooleanField()

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		return '/sitio/%s/' % (self.slug)

	class Meta:
		verbose_name_plural = "Videos"

def get_file_path(intance,filename):
	return os.path.join(intance.fileDir, filename)

class Talleres(models.Model):
	titulo = models.CharField(max_length=250)
	descripcion = models.TextField()
	arte = models.ImageField(upload_to=get_file_path)
	proximo = models.BooleanField()
	ponente = models.ForeignKey(User)
	fileDir = 'imgportadas/'

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = "Talleres"

class EnVivo(models.Model):
	url_video = models.CharField(max_length=200)
	url_chat = models.CharField(max_length=200)
	en_vivo = models.BooleanField()

	class Meta:
		verbose_name = 'EnVivo'
		verbose_name_plural = 'EnVivos'

	def __unicode__(self):
		return self.url_chat