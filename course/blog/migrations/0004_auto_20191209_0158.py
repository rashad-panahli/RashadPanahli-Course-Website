# Generated by Django 2.2.7 on 2019-12-09 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='context',
            new_name='post_context',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='post_date_posted',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='post_title',
        ),
    ]