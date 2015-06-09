# coding=utf-8
# -*- coding: utf-8 -*-
#models.py

#import os
#from django.conf import settings
from django.db import models

SZ_FBUSER_ID = 80
SZ_FBUSER_NAME = 250
SZ_PUBFIG = 64
SZ_VERB = 64
SZ_THING = 64
SZ_PREPOS = 16
SZ_PLACE = 64
SZ_TIME = 64

class FBUser(models.Model):
    fbid = models.CharField(max_length=SZ_FBUSER_ID, unique=True, verbose_name='fbid')
    name = models.CharField(max_length=SZ_FBUSER_NAME, unique=False, verbose_name='nome')
    inc_me = models.BooleanField(default=True, verbose_name='includimi nelle frasi')
    inc_pubfig = models.BooleanField(default=True, verbose_name='includi personaggi pubblici')
    alfasort = models.BooleanField(default=True, verbose_name='amici in ordine alfabetico')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creato il')
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.fbid)
    class Meta:
        db_table = u'fbuser'

class PubFig(models.Model):
    name = models.CharField(max_length=SZ_PUBFIG, unique=True, verbose_name='name')
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'pubfig'

class Verb(models.Model):
    name = models.CharField(max_length=SZ_VERB, unique=True, verbose_name='name')
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'verb'

class Thing(models.Model):
    name = models.CharField(max_length=SZ_THING, unique=True, verbose_name='name')
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'thing'

class Prepos(models.Model):
    name = models.CharField(max_length=SZ_PREPOS, unique=False, verbose_name='name')
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'prepos'

class Place(models.Model):
    name = models.CharField(max_length=SZ_PLACE, unique=True, verbose_name='name')
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'place'

class Time(models.Model):
    name = models.CharField(max_length=SZ_TIME, unique=True, verbose_name='name')
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'time'

