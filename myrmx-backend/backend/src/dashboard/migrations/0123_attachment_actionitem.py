# Generated by Django 2.0.5 on 2020-07-31 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0122_auto_20200731_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='actionItem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='dashboard.ActionItemAssessment'),
        ),
    ]
