# Generated by Django 3.2.3 on 2021-06-22 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calle',
            fields=[
                ('idCalle', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de la Calle')),
                ('nombreCalle', models.CharField(max_length=50, verbose_name='Nombre de la Calle')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCasa',
            fields=[
                ('idHogar', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id tipo casa')),
                ('nombreHogar', models.CharField(max_length=15, verbose_name='Nombre del tipo de casa')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('nombre', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='nombre')),
                ('direccion', models.CharField(max_length=30, verbose_name='direccion')),
                ('comuna', models.CharField(max_length=25, verbose_name='Comuna')),
                ('calle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.calle')),
                ('tipocasa', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tipocasa')),
            ],
        ),
    ]
