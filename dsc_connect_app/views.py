from .models import Dsc, User

from .serializers import (
    DscSerializer, 
    UserSerializer, 
    RegistrationSerializer)

from .permissions import (
    IsAdminOrSuperUser,
    CustomOrIsAdminOrSuperUserPermission,
    IsSuperUserOrReadOnly,
    IsSuperUser)

from rest_framework import viewsets, mixins, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class DscFilter(rest_framework.FilterSet):
	domains = rest_framework.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Dsc
		fields = ('domains', 'country', 'name')


class DscViewSet(mixins.CreateModelMixin, 
                mixins.RetrieveModelMixin, 
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = DscFilter


    def list(self, request):
        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)
        permission_classes = (AllowAny,)
        return Response({
         	'error':False,
         	'message': 'List of Dscs',
            'data': serializer.data,
         	},status =status.HTTP_200_OK )

    # def create(self, request):
    #     pass

    def retrieve(self, request, pk=None):
        lookup_field = 'pk'
        permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)

        return Response({
            'data': serializer.data,
            'error': False,
            'message': 'Your Dsc'
            }, status= status.HTTP_200_OK)

    def update(self, request, pk=None):
        lookup_field = 'pk'
        permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)

        return Response({
            'error': False,
            'data': serializer.data,
            'message': 'Dsc Updated Successfully',
            }, status= status.HTTP_200_OK)


    def partial_update(self, request, pk=None):
        lookup_field = 'pk'
        permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response({
            'data': serializer.data,
            'error': False,
            'message': 'Dsc Updated Successfully',
            }, status= status.HTTP_200_OK)


class UserAPIView( 
                generics.ListAPIView):
	
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        permission_classes = (IsAdminOrSuperUser,)
        filter_backends = [OrderingFilter]
        
        return Response({
         	'data': serializer.data,
         	'error': False,
         	'message':'List of Users',
            }, status = status.HTTP_200_OK)

class UserProfileAPIView(
    generics.RetrieveUpdateDestroyAPIView):

    def retrieve(self, request, pk=None):
        lookup_field = 'pk'
        permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response({
            'data': serializer.data,
            'error': False,
            'message': 'User Profile'
            }, status= status.HTTP_200_OK)


    def update(self, request, pk=None):
        lookup_field = 'pk'
        permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response({
            'data': serializer.data,
            'error': False,
            'message': 'User Profile Update Successfully',
            }, status= status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        lookup_field = 'pk'
        permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response({
            'data': serializer.data,
            'error': False,
            'message': 'User Profile Update Successfully',
            }, status= status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        lookup_field = 'pk'
        permission_classes = (IsAdminOrSuperUser,)
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response({
            'data': serializer.data,
            'error': False,
            'message': 'User Deleted Successfully'
            }, status= status.HTTP_200_OK)


class RegistrationView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
                        'error': False,
                        'message': 'Successfully registered. You can now login',    
                        'data':serializer.data,}, 
                        status=status.HTTP_201_CREATED)


class LoginView(ObtainJSONWebToken):
    
    def post(self, request, *args, **kwargs):
        # by default attempts username / passsword combination
        response = super(LoginView, self).post(request, *args, **kwargs)
        res = response.data
        token = res.get('token')

        # token ok, get user
        if token:
            user = jwt_decode_handler(token)  # aleady json - don't serialize
        else:  # if none, try auth by email
            req = request.data  # try and find email in request
            email = req.get('email')
            password = req.get('password')
            #username = req.get('username')

            if email is None or password is None:
                return Response({
                                'error': True, 
                                'message': 'Missing or incorrect credentials',
                                'data': req},
                                status=status.HTTP_400_BAD_REQUEST)

            # email exists in request, try to find user
            try:
                user = User.objects.get(email=email)
            except:
                return Response({
                                'error': True, 
                                'message': 'User not found',
                                'data': req},
                                status=status.HTTP_404_NOT_FOUND)

            if not user.check_password(password):
                return Response({'error': True, 
                                'message': 'Incorrect password',
                                'data': req},
                                status=status.HTTP_403_FORBIDDEN)

            # make token from user found by email
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            user = UserSerializer(user).data

        return Response({
                        'error': False,
                        'message': 'Successfully logged in',
                        'token': token,
                        'user': user }, 
                        status=status.HTTP_200_OK)
