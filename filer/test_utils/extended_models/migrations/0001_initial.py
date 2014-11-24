464# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attachment'
        db.create_table('extended_models_attachment', (
            ('file_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['filer.File'])),
        ))
        db.send_create_signal('extended_models', ['Attachment'])

        # Adding model 'AttachmentImage'
        db.create_table('extended_models_attachmentimage', (
            ('image_ptr', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['filer.Image'])),
            ('attachment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['extended_models.Attachment'])),
            ('attachment_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('extended_models', ['AttachmentImage'])


    def backwards(self, orm):
        # Deleting model 'Attachment'
        db.delete_table('extended_models_attachment')

        # Deleting model 'AttachmentImage'
        db.delete_table('extended_models_attachmentimage')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'extended_models.attachment': {
            'Meta': {'_ormbases': ['filer.File'], 'object_name': 'Attachment'},
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['filer.File']"})
        },
        'extended_models.attachmentimage': {
            'Meta': {'_ormbases': ['extended_models.Attachment', 'filer.Image'], 'object_name': 'AttachmentImage'},
            'attachment_description': ('django.db.models.fields.TextField', [], {}),
            'attachment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['extended_models.Attachment']"}),
            'image_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['filer.Image']"})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['filer.Folder']", 'related_name': "'all_files'"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'default': "''"}),
            'original_filename': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['auth.User']", 'related_name': "'owned_files'"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['contenttypes.ContentType']", 'related_name': "'polymorphic_filer.file_set'"}),
            'sha1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '40', 'default': "''"}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'filer.folder': {
            'Meta': {'object_name': 'Folder', 'unique_together': "(('parent', 'name'),)", 'ordering': "('name',)"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['auth.User']", 'related_name': "'filer_owned_folders'"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['filer.Folder']", 'related_name': "'children'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image'},
            '_height': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['filer.File']"}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '64', 'null': 'True', 'default': 'None'})
        }
    }

    complete_apps = ['extended_models']