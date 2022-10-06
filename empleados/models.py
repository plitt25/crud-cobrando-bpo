from django.db import models

# Create your models here.
    
class Departamento (models.Model):
    codigo= models.IntegerField()
    nombre=models.CharField(max_length=100)
    presupuesto=models.FloatField(max_length=100)
    def __str__(self):
        return "%s" % (self.codigo)
    
class Empleado (models.Model):
    codigo= models.IntegerField()
    nif=models.CharField(max_length=9)
    nombre=models.CharField(max_length=100)
    apellido1=models.CharField(max_length=100)
    apellido2=models.CharField(max_length=100)
    codigo_departamento=models.IntegerField()
    departamento= models.ForeignKey(Departamento, on_delete=models.CASCADE)
    def __str__(self):
        return self.codigo_departamento
    class Meta:
        ordering = ['codigo_departamento']