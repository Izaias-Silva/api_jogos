
from rest_framework import viewsets
from .models import Jogo
from .serializers import JogoSerializer

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
