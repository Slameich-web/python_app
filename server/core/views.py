# Create your view and viewsets here
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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
    
class SumApiView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly)
    def get(self, request):
        lst = Income.objects.all().values()
        print(request)
        return Response({'title': IncomeSerializer(lst, many=True).data})
