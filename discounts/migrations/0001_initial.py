# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'discounts_country', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 7, 22, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'discounts', ['Country'])

        # Adding model 'Company'
        db.create_table(u'discounts_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 7, 22, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discounts.Country'])),
        ))
        db.send_create_signal(u'discounts', ['Company'])

        # Adding unique constraint on 'Company', fields ['name', 'country']
        db.create_unique(u'discounts_company', ['name', 'country_id'])

        # Adding model 'Negotiator'
        db.create_table(u'discounts_negotiator', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'discounts', ['Negotiator'])

        # Adding model 'Agreement'
        db.create_table(u'discounts_agreement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_start', self.gf('django.db.models.fields.DateField')()),
            ('date_end', self.gf('django.db.models.fields.DateField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 7, 22, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discounts.Company'])),
            ('negotiator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discounts.Negotiator'])),
            ('export_turnover', self.gf('django.db.models.fields.FloatField')(default=0, blank=True)),
            ('import_turnover', self.gf('django.db.models.fields.FloatField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'discounts', ['Agreement'])

        # Adding unique constraint on 'Agreement', fields ['company', 'date_start', 'date_end']
        db.create_unique(u'discounts_agreement', ['company_id', 'date_start', 'date_end'])

        # Adding model 'Period'
        db.create_table(u'discounts_period', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_start', self.gf('django.db.models.fields.DateField')()),
            ('date_end', self.gf('django.db.models.fields.DateField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 7, 22, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('agreement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discounts.Agreement'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'discounts', ['Period'])


    def backwards(self, orm):
        # Removing unique constraint on 'Agreement', fields ['company', 'date_start', 'date_end']
        db.delete_unique(u'discounts_agreement', ['company_id', 'date_start', 'date_end'])

        # Removing unique constraint on 'Company', fields ['name', 'country']
        db.delete_unique(u'discounts_company', ['name', 'country_id'])

        # Deleting model 'Country'
        db.delete_table(u'discounts_country')

        # Deleting model 'Company'
        db.delete_table(u'discounts_company')

        # Deleting model 'Negotiator'
        db.delete_table(u'discounts_negotiator')

        # Deleting model 'Agreement'
        db.delete_table(u'discounts_agreement')

        # Deleting model 'Period'
        db.delete_table(u'discounts_period')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'discounts.agreement': {
            'Meta': {'unique_together': "(('company', 'date_start', 'date_end'),)", 'object_name': 'Agreement'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['discounts.Company']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 7, 22, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'export_turnover': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_turnover': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'negotiator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['discounts.Negotiator']"})
        },
        u'discounts.company': {
            'Meta': {'unique_together': "(('name', 'country'),)", 'object_name': 'Company'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['discounts.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 7, 22, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'discounts.country': {
            'Meta': {'object_name': 'Country'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 7, 22, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3', 'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'discounts.negotiator': {
            'Meta': {'object_name': 'Negotiator', '_ormbases': [u'auth.User']},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'discounts.period': {
            'Meta': {'object_name': 'Period'},
            'agreement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['discounts.Agreement']"}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 7, 22, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['discounts']