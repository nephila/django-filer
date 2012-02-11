# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('filer.views',
    url(r'^filer/', 'tinymce_filer', name="tinymce-filer"),
 )
