# Generated by Django 2.0.5 on 2019-09-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_company_users_can_assign_coach'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='coach_synonym',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]