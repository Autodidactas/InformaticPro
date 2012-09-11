# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField

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

class Videos(models.Model):
	titulo = models.CharField(max_length=200)
	fecha = models.DateField()
	descripcion = models.TextField('Descripción')
	url = models.URLField()
	tags = TagAutocompleteField("Tags",help_text='Separar elementos con "," ', null=True, blank=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True)
	curso = models.ForeignKey(Cursos, null=True, blank=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = "Videos"


		