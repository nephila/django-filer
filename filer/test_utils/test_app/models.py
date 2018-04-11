# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models

from ...fields.file import FilerFileField
from ...fields.folder import FilerFolderField
from ...fields.image import FilerImageField


class MyModel(models.Model):

    general = FilerFileField(related_name='test_file')
    image = FilerImageField(related_name='test_image')
    folder = FilerFolderField(related_name='test_folder')


class InlineModel(models.Model):
    parent = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    image = FilerImageField(related_name='test_image2')
