# Generated by Django 2.1.2 on 2018-11-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spew', '0010_auto_20181031_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='num_credits',
            field=models.TextField(default='', help_text='Enter a brief description of the class', max_length=1000),
            preserve_default=False,
        ),
    ]