# Generated by Django 2.0.5 on 2019-12-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0090_auto_20191202_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='show_print_competency_detail_button',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='y6sH886B6Uaz04crkAK5BxKpKEUE0EVEeL3ZKkOz5oYbcjf9uZR5ZSz2PMpSRsCKJOeyr3r1VBC'),
        ),
    ]