from main.models import Curso, Direccion, Estudiante, Profesor

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
def crear_direccion(calle,numero,comuna,region,estudiante_rut):
    e = Estudiante.objects.get(rut=estudiante_rut)
    d = Direccion(calle=calle,numero=numero,comuna=comuna,region=region,estudiante=e)
    d.save()
    return d
def obtiene_estudiante(estudiante_rut):
    e = Estudiante.objects.get(rut=estudiante_rut)
    return e
def obtiene_profesor(profesor_rut):
    p = Profesor.objects.get(rut=profesor_rut)
    return p
def obtiene_curso(curso_codigo):
    c = Curso.objects.get(codigo=curso_codigo)
    return c
def agrega_profesor_a_curso(profesor_rut, curso_codigo):
    p = Profesor.objects.get(rut=profesor_rut)
    c = Curso.objects.get(codigo=curso_codigo)
    c.profesor = p
    c.save()
def agrega_cursos_a_estudiante(curso_codigo, estudiante_rut):
    c = Curso.objects.get(codigo=curso_codigo)
    e = Estudiante.objects.get(rut=estudiante_rut)
    c.estudiantes.add(e)
def imprime_estudiante_cursos(estudiante_rut):
    estudiante = obtiene_estudiante(estudiante_rut)
    print(f'Cursos del estudiante {estudiante.nombre} {estudiante.apellido}')
    cursos = estudiante.cursos.all()
    for curso in cursos:
        print(f'    {curso.nombre}')