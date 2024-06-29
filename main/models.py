from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Direccion(models.Model):
    #regiones = (('i', 'Tarapacá'),('ii', 'Antofagasta'),('iii', 'Atacama'),('iv', 'Coquimbo'),('v', 'Valparaíso'),('vi', "O'Higgins"),('vii', 'Maule'),('viii', 'Ñuble'),('ix', 'Biobío'),('x', 'La Araucanía'),('xi', 'Los Ríos'),('xii', 'Los Lagos'),('xiv', 'Los Ríos'),('xv', 'Aysén'),('xvi', 'Magallanes y de la Antártica Chilena'),('rm', 'Región Metropolitana de Santiago'))
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    #relacion uno a uno
    estudiante = models.OneToOneField(Estudiante, related_name='direccion', on_delete=models.CASCADE)

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor = models.ForeignKey(Profesor, related_name='cursos',null=True, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')
