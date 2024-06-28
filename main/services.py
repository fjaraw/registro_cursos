from main.models import *

def crear_curso(codigo,nombre,version,profesor):
    c = Curso(codigo=codigo,nombre=nombre,version=version,profesor=profesor)
    c.save()
    return c
def crear_profesor(rut,nombre,apellido):
    p = Profesor(rut=rut,nombre=nombre,apellido=apellido,activo=True)
    p.save()
    return p
def crear_estudiante(rut,nombre,apellido,fecha_nacimiento):
    e = Estudiante(rut=rut,nombre=nombre,apellido=apellido,fecha_nacimiento=fecha_nacimiento,activo=True)
    e.save()
    return e
def crear_direccion():
    pass
def obtiene_estudiante():
    pass
def obtiene_profesor():
    pass
def obtiene_curso():
    pass
def agrega_profesor_a_curso():
    pass
def agrega_cursos_a_estudiante():
    pass
def imprime_estudiante_cursos():
    pass