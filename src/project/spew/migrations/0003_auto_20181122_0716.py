# Generated by Django 2.1.2 on 2018-11-22 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spew', '0002_auto_20181106_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='spewuser',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='spewuser',
            name='password1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='spewuser',
            name='password2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='spewuser',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='spewuser',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='spewuser',
            name='major',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='spew.Subject'),
        ),
    ]
