# Generated by Django 2.1.2 on 2018-11-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spew', '0021_remove_user_current_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fav_courses',
            field=models.ManyToManyField(help_text='Select the classes this user favorites', to='spew.Class'),
        ),
    ]