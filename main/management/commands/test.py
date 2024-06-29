from typing import Any
from main.services import *
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('Modulo de prueba.')
        #e = crear_estudiante('111111111','John','Doe','2000-01-01')
        #p = crear_profesor('088888888','Profesor','Salomon')
        #c = crear_curso('KL01','Introducción al Klingon',1,p)
        #print(e)
        #print(p)
        #agrega_cursos_a_estudiante('KL01', '111111111')
        #crear_curso('M01','Aritmética',1)
        #agrega_profesor_a_curso('088888888', 'M01')
        #agrega_cursos_a_estudiante('M01', '111111111')
        imprime_estudiante_cursos('111111111')
        print('Operacion(es) realizada(s).')