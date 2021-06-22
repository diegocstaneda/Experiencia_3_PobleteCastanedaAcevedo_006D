from django.db import models

# Create your models here.
class Calle(models.Model):
    idCalle=models.IntegerField(primary_key=True, verbose_name='Id de la Calle')
    nombreCalle=models.CharField(max_length=50, verbose_name='Nombre de la Calle')

    def __str__(self):
        return self.nombreCalle

class TipoCasa(models.Model):
    idHogar=models.IntegerField(primary_key=True, verbose_name='Id tipo casa')
    nombreHogar=models.CharField(max_length=15, verbose_name='Nombre del tipo de casa')

    def __str__(self):
        return self.nombreHogar

class Direccion(models.Model):
    nombre = models.CharField(max_length=25, primary_key=True, verbose_name='nombre')
    direccion = models.CharField(max_length=30, verbose_name='direccion')
    comuna = models.CharField(max_length=25, verbose_name='Comuna')
    calle = models.ForeignKey(Calle, on_delete=models.CASCADE)
    tipocasa = models.ForeignKey(TipoCasa, default='', on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.nombre