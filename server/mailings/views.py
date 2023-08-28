from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from mailings.models import Mailing
from mailings.serializers import MailingSerializer


class MailingsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = MailingSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'start_time': ['lt', 'gt']
    }

    def get_queryset(self):
        return Mailing.objects.all()
