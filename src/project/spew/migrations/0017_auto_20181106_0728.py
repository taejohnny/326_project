# Generated by Django 2.1.2 on 2018-11-06 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spew', '0016_merge_20181106_0236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='course',
            new_name='fav_courses',
        ),
        migrations.RemoveField(
            model_name='class',
            name='class_feedback',
        ),
    ]