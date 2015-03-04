# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0010_auto_20150303_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_key',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=b'NULL', upload_to=b''),
            preserve_default=True,
        ),
    ]
