# Generated by Django 2.0.5 on 2020-04-19 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0108_auto_20200414_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='followupitem',
            name='attempted_to_contact',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='followupitem',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='followupitem',
            name='no_attempt_to_contact',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='followupitem',
            name='notes',
            field=models.TextField(blank=True, max_length=2024, null=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='tbY0DIrStYLuNptasqWoQbxGCy8TmaIQkQStriuGsJbz0xEyWWBu7EtI8M4ieMCnWDlcGdejAOQ'),
        ),
    ]
