from rest_framework import viewsets
from games.models import Game
from games.serializers import GameSerializer


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
