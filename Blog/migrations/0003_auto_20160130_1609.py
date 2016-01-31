# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20160127_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe7\xb1\xbb', blank=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
