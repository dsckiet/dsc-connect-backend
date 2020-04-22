

from dsc_connect_app.views import (
	ApiRoot,
	DscListAPIView,
	DscDetailAPIView, 
	UserAPIView, 
	UserProfileAPIView, 
	LoginView,
	RegistrationView)
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
	path('', ApiRoot.as_view()),
	path('api/v1/dsc/users/', UserAPIView.as_view(), name='user-list'),
	path('api/v1/dsc/users/<pk>/', UserProfileAPIView.as_view(), name='user-profile'),
	path('api/v1/dsc/', DscListAPIView.as_view(), name ='dsc-list'),
	path('api/v1/dsc/<pk>/', DscDetailAPIView.as_view(), name ='dsc-detail'),
	path('api/v1/signup/', RegistrationView.as_view(), name = 'signup'),
    path('api/v1/login/', LoginView.as_view(), name = 'login'),
])