# Create your view and viewsets here
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import mixins, viewsets, views
from rest_framework.response import Response

from core.models import BotSettings, TelegramMedia
from core.serializers import BotSettingsSerializer, TelegramMediaSerializer
from users.models import User
from income.models import Income

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_id', 'first_name')

#class UserApiView(generics.ListAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer
    
    
class IncomeSerializer(serializers.ModelSerializer):
    total = serializers.CharField()
    calculation_date = serializers.DateTimeField()
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Income
        fields = ('total', 'calculation_date', 'user')

class UserApiView(APIView):
    def get(self, request):
        lst = User.objects.all().values()
        return Response({'title': list(lst)})
    
class BotSettingsView(
    views.APIView,
):
    def get_object(self):
        return BotSettings.objects.last()

    def get(self, request):
        settings = self.get_object()

        settings_serializer = BotSettingsSerializer(settings)

        return Response(settings_serializer.data)


class UpdateTelegramMediaView(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = TelegramMediaSerializer

    def get_queryset(self):
        return TelegramMedia.objects.all()

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
