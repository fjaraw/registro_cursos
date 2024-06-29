from main.models import Curso, Estudiante, Profesor

def crear_curso(codigo,nombre,version):
    #p = Profesor.objects.get(rut=profesor_rut)
    c = Curso(codigo=codigo,nombre=nombre,version=version)
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
def agrega_profesor_a_curso(profesor_rut, curso_codigo):
    p = Profesor.objects.get(rut=profesor_rut)
    c = Curso.objects.get(codigo=curso_codigo)
    c.profesor = p
    c.save()
def agrega_cursos_a_estudiante(curso_codigo, estudiante_rut):
    c = Curso.objects.get(codigo=curso_codigo)
    e = Estudiante.objects.get(rut=estudiante_rut)
    c.estudiantes.add(e)
def imprime_estudiante_cursos():
    pass