# Generated by Django 2.0.5 on 2020-04-15 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('dashboard', '0106_auto_20200406_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Company')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
            ],
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='CSbeEJNB6XRJPH2XJVB42UugDOu5ktHy1SGYva19UEUn5tf1tyoRWba9oBIfppt9OjNLReURORV'),
        ),
        migrations.AddField(
            model_name='user',
            name='assigned_companies',
            field=models.ManyToManyField(blank=True, related_name='assigned_company_users', to='dashboard.AssignedCompany'),
        ),
    ]
