# Generated by Django 3.2.3 on 2021-06-22 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='numedirec',
            field=models.CharField(default='', max_length=3, verbose_name='numerdir'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='telefono',
            field=models.CharField(default='', max_length=9, verbose_name='telefono,'),
        ),
    ]
