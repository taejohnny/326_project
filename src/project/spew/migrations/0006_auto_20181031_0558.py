# Generated by Django 2.1.2 on 2018-10-31 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spew', '0005_auto_20181030_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spew.Subject'),
        ),
    ]