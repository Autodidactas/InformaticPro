# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table('sitio_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('sitio', ['Categoria'])

        # Adding model 'Cursos'
        db.create_table('sitio_cursos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('sitio', ['Cursos'])

        # Adding model 'Redes'
        db.create_table('sitio_redes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('sitio', ['Redes'])

        # Adding model 'UserProfile'
        db.create_table('sitio_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('sitio', ['UserProfile'])

        # Adding model 'Social'
        db.create_table('sitio_social', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('red', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sitio.Redes'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sitio.UserProfile'])),
        ))
        db.send_create_signal('sitio', ['Social'])

        # Adding model 'Videos'
        db.create_table('sitio_videos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sitio.Categoria'], null=True, blank=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sitio.Cursos'], null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('portada', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('sitio', ['Videos'])

        # Adding model 'Talleres'
        db.create_table('sitio_talleres', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('arte', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('proximo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ponente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('sitio', ['Talleres'])

        # Adding model 'EnVivo'
        db.create_table('sitio_envivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('url_video', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url_chat', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('en_vivo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ponente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('sitio', ['EnVivo'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table('sitio_categoria')

        # Deleting model 'Cursos'
        db.delete_table('sitio_cursos')

        # Deleting model 'Redes'
        db.delete_table('sitio_redes')

        # Deleting model 'UserProfile'
        db.delete_table('sitio_userprofile')

        # Deleting model 'Social'
        db.delete_table('sitio_social')

        # Deleting model 'Videos'
        db.delete_table('sitio_videos')

        # Deleting model 'Talleres'
        db.delete_table('sitio_talleres')

        # Deleting model 'EnVivo'
        db.delete_table('sitio_envivo')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sitio.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sitio.cursos': {
            'Meta': {'object_name': 'Cursos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sitio.envivo': {
            'Meta': {'object_name': 'EnVivo'},
            'en_vivo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ponente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url_chat': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url_video': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sitio.redes': {
            'Meta': {'object_name': 'Redes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sitio.social': {
            'Meta': {'object_name': 'Social'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'red': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sitio.Redes']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sitio.UserProfile']"})
        },
        'sitio.talleres': {
            'Meta': {'object_name': 'Talleres'},
            'arte': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ponente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'proximo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'sitio.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'sitio.videos': {
            'Meta': {'object_name': 'Videos'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sitio.Categoria']", 'null': 'True', 'blank': 'True'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sitio.Cursos']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['sitio']