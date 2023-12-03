from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from barberia_app.models import Turno
from barberia_app.serializers import TurnoSerializer

# Create your views here.
class TurnoAPI(APIView):
    def post(self, request):
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)