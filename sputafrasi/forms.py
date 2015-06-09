# coding=utf-8
# -*- coding: utf-8 -*-

# forms.py
from django import forms
from django.forms.widgets import HiddenInput
import models

class UserPrefForm(forms.ModelForm):
    class Meta:
        model = models.FBUser
        widgets = {
            'fbid' : HiddenInput(),
            'name' : HiddenInput(),
        }
#        fields  = ('inc_me', 'inc_pubfig', 'alfasort')
#        exclude = ('fbid', 'name', )
