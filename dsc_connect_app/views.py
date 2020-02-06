from .models import Dsc, STATUS_CHOICES
from .serializers import DscSerializers
from .permissions import IsOwnerOrReadOnly
from django.core.exceptions import ValidationError
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.reverse import reverse


#api-root page will show the list of all verified dscs
class Api_root(APIView):
	queryset = Dsc.objects.filter(status = '1')
	serializer_class = DscSerializers

# view to show list of all DSCs and register one if not already registered!!
class DscList(generics.ListCreateAPIView):
	queryset = Dsc.objects.filter(status = '1')
	serializer_class = DscSerializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		queryset = Dsc.objects.filter(author = self.request.user)
		serializer_class = SerializerWithoutstatusField
		if queryset.exists():
			raise ValidationError('You already lead a Dsc!!')
		serializer.save(author = self.request.user, status = STATUS_CHOICES[0][0])

# view to show and update Dsc model if user is authenticated and Owner respectively #
class DscDetail(generics.RetrieveUpdateAPIView):
	queryset = Dsc.objects.all()
	serializer_class = DscSerializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

	def perform_update(self,serializer):
		queryset = Dsc.objects.filter(author = self.request.user)
		serializer_class = SerializerWithoutstatusField
		serializer.save(author = self.request.user, status = STATUS_CHOICES[0][0])
