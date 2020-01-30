from .models import Dsc
from .serializers import DscSerializers
from .permissions import IsOwnerOrReadOnly
from django.core.exceptions import ValidationError
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

#api-root page will show the list of all verified dscs
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'dsc_connect_app': reverse('dsc-list', request = request, format = format)
    })


# view to show list of all DSCs and register one if not already registered!!
class DscList(generics.ListCreateAPIView):
	queryset = Dsc.objects.all()
	serializer_class = DscSerializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		queryset = Dsc.objects.filter(author = self.request.user)
		if queryset.exists():
			raise ValidationError('You already lead a Dsc!!')
		serializer.save(author = self.request.user)

# view to show and update Dsc model if user is authenticated and Owner respectively #
class DscDetail(generics.RetrieveUpdateAPIView):
	queryset = Dsc.objects.all()
	serializer_class = DscSerializers
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


