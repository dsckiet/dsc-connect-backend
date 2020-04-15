

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
	path('dsc/users/', UserAPIView.as_view(), name='user-list'),
	path('dsc/users/(?P<pk>[0-9]+)/', UserProfileAPIView.as_view(), name='user-profile'),
	path('dsc/', DscListAPIView.as_view(), name ='dsc-list'),
	path('dsc/(?P<pk>[0-9]+)/', DscDetailAPIView.as_view(), name ='dsc-detail'),
	path('signup/', RegistrationView.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(), name = 'login'),
])