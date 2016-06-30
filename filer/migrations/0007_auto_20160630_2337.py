# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file_ptr',
            field=models.OneToOneField(related_name='filer_image_file', primary_key=True, serialize=False, to='filer.File'),
        ),
    ]
