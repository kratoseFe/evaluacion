from django.db import models

# Create your models here.
class Estudianate(models.Model):
    nombre = models.CharField(max_length=20)
    ficha = models.IntegerField()
    edad = models.IntegerField()


    class Meta:
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

    def __str__(self):
        return self.nombre