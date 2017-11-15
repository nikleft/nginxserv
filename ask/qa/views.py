# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import os
from django.http import HttpResponse
from django.conf import settings
#os.environ['DJANGO_SETTINGS_MODULE']='ask.settings'

settings.configure(DEFAULT_CONTENT_TYPE='text/html')
def test(request,*args,**kwargs):
	return HttpResponse('OK')



# Create your views here.
