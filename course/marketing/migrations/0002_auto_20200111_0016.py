# Generated by Django 2.2.7 on 2020-01-11 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='email',
            new_name='mail',
        ),
    ]
