# Generated by Django 2.0.5 on 2019-10-22 15:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0059_auto_20191018_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='competency',
            name='hidden_for',
            field=models.ManyToManyField(blank=True, related_name='hidden_for', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='K6H56RhniL8UctxVccvxisyWJA9aZDHq7DZKV0yitk07jQGQe9hQVksHpHxgAaYZw0vrm5weffO'),
        ),
    ]