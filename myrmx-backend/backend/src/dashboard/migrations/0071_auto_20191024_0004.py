# Generated by Django 2.0.5 on 2019-10-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0070_auto_20191023_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='assign_roadmaps_to_all_users',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='dbfFWVBn8A7zHcJNyAscxYpsSVUmuppcm9hXbRUbRZXLAQDL5fq5puB8cR2eYC6LJnJggEspyzy'),
        ),
    ]