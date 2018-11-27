# Generated by Django 2.1.2 on 2018-11-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spew', '0009_auto_20181126_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='concentration',
            field=models.CharField(default='Software Engineering', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='num_classes_taken',
            field=models.CharField(default='', help_text='# of classes taken by this user', max_length=1000),
        ),
        migrations.AlterField(
            model_name='student',
            name='num_liked_reviews',
            field=models.CharField(default='', help_text='# of reviews this user liked', max_length=1000),
        ),
    ]
