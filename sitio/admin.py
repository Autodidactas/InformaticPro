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
	#prepopulated_fields = {"slug": ("titulo",)}
	list_display = ('fecha', 'usuario','titulo','portada','curso','categoria')
	search_fields = ['titulo']
	list_filter = ('usuario','categoria','curso')
	date_hierarchy = 'fecha'

	class Media:
		js = ('js/tiny_mce/tiny_mce.js',
              'js/basic_config.js',)

class TalleresAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'ponente',)
	search_fields = ['titulo']
	list_filter = ('ponente',)

	class Media:
		js = ('js/tiny_mce/tiny_mce.js',
              'js/basic_config.js',)

admin.site.register(Videos, VideosAdmin)
admin.site.register(Talleres, TalleresAdmin)
admin.site.register(Categoria)
admin.site.register(Cursos)
admin.site.register(Redes)
admin.site.register(EnVivo)
