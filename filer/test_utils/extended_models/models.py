# -*- coding: utf-8 -*-
from django.db import models
from filer.models import File, Image


class Attachment(File):

    class Meta:
        app_label = 'extended_models'


class AttachmentImage(Attachment, Image):
    attachment_description = models.TextField()

    class Meta:
        app_label = 'extended_models'