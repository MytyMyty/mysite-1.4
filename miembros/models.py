from django.db import models

class Miembros(models.Model):
    rut= models.CharField(primary_key=True, max_length=10)
    mail= models.EmailField(unique=True, max_length=100)
    nombre= models.CharField(max_length=30)
    apellidos= models.CharField(max_length=80)
    password1=models.CharField(max_length=340)
    fecnac= models.DateField(blank=False, null=False)
    activo= models.IntegerField()

    def  __str__(self):
        return str(self.nombre)+" "+str(self.apellidos)
    

# Create your models here.
