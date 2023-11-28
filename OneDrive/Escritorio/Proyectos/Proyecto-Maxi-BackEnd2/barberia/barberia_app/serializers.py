from rest_framework import serializers
from barberia_app.models import Turno

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ('fecha', 'especialidad', 'servicio', 'profesional', 'hora')
