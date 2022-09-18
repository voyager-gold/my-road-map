# Generated by Django 2.0.5 on 2018-12-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionitemassessment',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='unsubscribed',
            field=models.BooleanField(default=False),
        ),
    ]