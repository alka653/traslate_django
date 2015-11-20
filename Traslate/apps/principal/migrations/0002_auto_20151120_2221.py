# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traslate',
            name='dest_languaje',
            field=models.ForeignKey(related_name='d_languaje', default=1, blank=True, to='principal.Languaje'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traslate',
            name='dest_word',
            field=models.ForeignKey(related_name='d_word', default=1, blank=True, to='principal.Word'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='traslate',
            name='origin_languaje',
            field=models.ForeignKey(related_name='o_languaje', blank=True, to='principal.Languaje'),
        ),
        migrations.AlterField(
            model_name='traslate',
            name='origin_word',
            field=models.ForeignKey(related_name='o_word', blank=True, to='principal.Word'),
        ),
    ]
