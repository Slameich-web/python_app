# Create your view and viewsets here
from rest_framework import generics, serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_id', 'first_name')

class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer