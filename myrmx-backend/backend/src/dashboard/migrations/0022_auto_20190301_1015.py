# Generated by Django 2.0.5 on 2019-03-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_user_valid_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionitemassessment',
            name='description',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='actionitemassessment',
            name='notes',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
