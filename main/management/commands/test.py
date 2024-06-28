from typing import Any
from main.services import *
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('Modulo de prueba.')
        #e = crear_estudiante('111111111','John','Doe','2000-01-01')
        p = crear_profesor('088888888','Profesor','Salomon')
        c = crear_curso('KL01','Introducción al Klingon',1,p)
        #print(e)
        print(p)
        print('Operacion(es) realizada(s).')