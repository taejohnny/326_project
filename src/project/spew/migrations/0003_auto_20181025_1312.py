# Generated by Django 2.1.2 on 2018-10-25 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spew', '0002_auto_20181023_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='favorite_classes',
            new_name='course',
        ),
    ]