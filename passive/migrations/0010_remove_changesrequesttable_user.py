# Generated by Django 4.0.4 on 2022-07-13 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passive', '0009_changesrequesttable_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='changesrequesttable',
            name='user',
        ),
    ]