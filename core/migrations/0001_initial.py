# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EyeLid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.TextField()),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('region', models.CharField(max_length=1000)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Study'),
        ),
        migrations.AddField(
            model_name='eyelid',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient'),
        ),
    ]
