# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib import admin

from .models import MyModel, InlineModel


class InlineModelInline(admin.TabularInline):
    model = InlineModel

class MyModelAdmin(admin.ModelAdmin):
    model = MyModel
    inlines = (InlineModelInline,)

admin.site.register(MyModel, MyModelAdmin)
