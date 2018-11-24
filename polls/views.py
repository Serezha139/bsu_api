from rest_framework import viewsets
from polls.models import Poll
from polls.serializers import PollSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
