from django.test import TestCase
from django.utils import timezone
from .models import Turno


# Create your tests here.
class TurnoTestCase(TestCase):
    def setUp(self):
         self.turno = Turno.objects.create(fecha=timezone.now().date(), especialidad=self.especialidad,servicio=self.servicio,profesional=self.profesional,hora=timezone.now().time())

