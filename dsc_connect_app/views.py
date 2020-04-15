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
from rest_framework.reverse import reverse  
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from django_filters import rest_framework

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class ApiRoot(generics.ListAPIView):
    permission_classes = (AllowAny,)
    def list(self, request, format = None):
        return Response({
            'dsc_connect_app': reverse('dsc-list', request = request, format=format),
            'users':reverse('user-list', request = request, format=format),
            'signup':reverse('signup', request = request, format=format),
            'login':reverse('login', request = request, format=format)
            })




class DscFilter(rest_framework.FilterSet):
 	domains = rest_framework.CharFilter(lookup_expr='icontains')
 	class Meta:
 		model = Dsc
 		fields = ('domains', 'country', 'name')


class DscListAPIView(
    generics.ListCreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = DscSerializer
    
    def list(self, request):
        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)
        permission_classes = (AllowAny,)
        filter_backends = [DjangoFilterBackend]
        filterset_class = DscFilter

        return Response({
         	'error':False,
         	'message': 'List of Dscs',
            'data': serializer.data,
         	},status =status.HTTP_200_OK )

    #TODO
    def create(self, request):
        permission_classes = (IsAuthenticated)
        queryset1 = Dsc.objects.filter(author = self.request.user)
        if queryset1.exists():
            return Response({
                'error': True,
                'message': 'You already have a Dsc registered'
                },status= status.HTTP_403_FORBIDDEN)

        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({
                'data': serializer.data,
                'error': False,
                'message': 'Dsc information Update Successfully',
                }, status= status.HTTP_200_OK)
        else:
            return Response({
                'error': True,
                'message': serializer.errors
                },status= status.HTTP_400_BAD_REQUEST)


class DscDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView):  

    def retrieve(self, request, pk=None):
        try:
            lookup_field = 'pk'
        except NotFound:
            return Response({
                'error': True,
                'message':'No match to query found'
                },status = status.HTTP_404_NOT_FOUND)
        try:
            permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        except PermissionDenied:
            return Response({
                'error': True,
                'message': 'You are not authorised to this page'
                }, status= status.HTTP_403_FORBIDDEN)
        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)

        return Response({
            'data': serializer.data,
            'error': False,
            'message': 'Your Dsc'
            }, status= status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            lookup_field = 'pk'
        except NotFound:
            return Response({
                'error': True,
                'message':'No match to query found'
                },status = status.HTTP_404_NOT_FOUND)
        try:
            permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        except PermissionDenied:
            return Response({
                'error': True,
                'message': 'You are not authorised to this page'
                }, status= status.HTTP_403_FORBIDDEN)
        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({
                'data': serializer.data,
                'error': False,
                'message': 'Dsc information Update Successfully',
                }, status= status.HTTP_200_OK)
        else:
            return Response({
                'error': True,
                'message': serializer.errors
                },status= status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk=None):
        try:
            lookup_field = 'pk'
        except NotFound:
            return Response({
                'error': True,
                'message':'No match to query found'
                },status = status.HTTP_404_NOT_FOUND)
        try:
            permission_classes = (CustomOrIsAdminOrSuperUserPermission,)
        except PermissionDenied:
            return Response({
                'error': True,
                'message': 'You are not authorised to this page'
                }, status= status.HTTP_403_FORBIDDEN)
        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({
                'data': serializer.data,
                'error': False,
                'message': 'Dsc information Update Successfully',
                }, status= status.HTTP_200_OK)
        else:
            return Response({
                'error': True,
                'message': serializer.errors
                } ,status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            lookup_field = 'pk'
        except NotFound:
            return Response({
                'error': True,
                'message':'No match to query found'
                } ,status = status.HTTP_404_NOT_FOUND)
        try:
            permission_classes = (IsAdminOrSuperUser,)
        except PermissionDenied:
            return Response({
                'error': True,
                'message': 'You are not authorised to delete'
                }, status= status.HTTP_403_FORBIDDEN)
        queryset = Dsc.objects.all()
        serializer = DscSerializer(queryset, many=True)

        return Response({
            'data': serializer.data,
            'error': False,
            'message': 'Dsc Deleted Successfully'
            }, status= status.HTTP_200_OK)


class UserAPIView( 
                generics.ListAPIView):
	
    permission_classes = (AllowAny,)
    
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
        # token = response.data['token']  # don't use this to prevent errors
        # below will return null, but not an error, if not found :)
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
