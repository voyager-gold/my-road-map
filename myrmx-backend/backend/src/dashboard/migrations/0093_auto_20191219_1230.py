# Generated by Django 2.0.5 on 2019-12-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0092_auto_20191219_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='gZQEQJCpU7KTk8CcWQNfjxtRimfF7Wsf2rcSMKST6PXVNU6yV0XSr2IOmnEEI87HgkVcUZnoVQi'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email_welcome_message',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
    ]
