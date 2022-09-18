# Generated by Django 2.0.5 on 2019-12-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20190206_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='verb',
            field=models.CharField(choices=[('COMMENTED', 'commented on'), ('NEEDS_APPROVAL', 'needs approval on'), ('APPROVED', 'approved assessment for'), ('NEEDS_WORK', 'marked assessment as needs work for'), ('NEW_USER', 'New account'), ('NEW_ACTION_ITEM', 'created an action item for'), ('AI_NEEDS_APPROVAL', 'needs approval for an action item on'), ('AI_APPROVED', 'approved action item for')], max_length=255),
        ),
    ]