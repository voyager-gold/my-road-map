# Generated by Django 2.0.5 on 2019-10-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0041_company_dark_ui'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='competency_notes_journal_section',
            field=models.BooleanField(default=True),
        ),
    ]
