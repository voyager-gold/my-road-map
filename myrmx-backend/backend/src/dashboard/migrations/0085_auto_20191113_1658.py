# Generated by Django 2.0.5 on 2019-11-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0084_auto_20191112_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='XjFwe2tqSVH8GiUL7lYLcREyvEA3g6abHQ0PXsfuU0RLYBfnZnuyYzFatxSFxwwwlOqvY4HvoEo'),
        ),
        migrations.AlterField(
            model_name='competency',
            name='green_description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='competency',
            name='red_description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='competency',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='competency',
            name='yellow_description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='roadmap',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='roadmap',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
