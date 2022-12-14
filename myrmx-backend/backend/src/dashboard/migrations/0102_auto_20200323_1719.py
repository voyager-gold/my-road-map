# Generated by Django 2.0.5 on 2020-03-23 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0101_auto_20200319_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedRoadmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_coach', to=settings.AUTH_USER_MODEL)),
                ('roadmap', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Roadmap')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='x7Xnt80PVeYRKve5BP4JxJaKCQLzvRf0TkyPUQTuBndfgE4vZFqjTrjw25mR06Wa20mvcl0LWvw'),
        ),
        migrations.AddField(
            model_name='user',
            name='assigned_roadmaps',
            field=models.ManyToManyField(blank=True, related_name='assigned_users', to='dashboard.AssignedRoadmap'),
        ),
    ]
