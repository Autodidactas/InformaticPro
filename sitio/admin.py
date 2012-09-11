from django.contrib import admin
from models import *

class SocialInline(admin.TabularInline):
	model = Social

class UserProfileAdmin(admin.ModelAdmin):
	inlines = [SocialInline]

admin.site.register(UserProfile, UserProfileAdmin)

class VideosAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'usuario',)

admin.site.register(Videos, VideosAdmin)
admin.site.register(Categoria)
admin.site.register(Cursos)
admin.site.register(Redes)
