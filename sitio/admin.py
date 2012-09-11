from django.contrib import admin
from models import *

class SocialInline(admin.TabularInline):
	model = Social
	extra = 1

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user','descripcion')
	search_fields = ['user']
	list_filter = ('user',)

	inlines = [SocialInline]

admin.site.register(UserProfile, UserProfileAdmin)

class VideosAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'usuario','titulo')
	search_fields = ['titulo']
	list_filter = ('usuario','categoria','curso')
	date_hierarchy = 'fecha'

admin.site.register(Videos, VideosAdmin)
admin.site.register(Categoria)
admin.site.register(Cursos)
admin.site.register(Redes)
