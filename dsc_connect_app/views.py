from .models import Dsc, User

from .serializers import DscSerializer, UserSerializer
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

class DscFilter(rest_framework.FilterSet):
	domains = rest_framework.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Dsc
		fields = ('domains', 'country', 'name')


class DscViewSet(viewsets.ModelViewSet):
    serializer_class = DscSerializer
    queryset = Dsc.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = DscFilter
    permission_class = []

class UserViewset(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_class = []
	