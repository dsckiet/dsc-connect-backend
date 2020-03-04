

from dsc_connect_app.views import (
	DscViewSet, 
	UserAPIView, 
	UserProfileAPIView, 
	LoginView,
	RegistrationView)
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

router = DefaultRouter()
router.register(r'dsc', DscViewSet, basename='dsc')
urlpatterns = router.urls
urlpatterns += [
	url(r'user/$', UserAPIView.as_view(), name='user-list'),
	url(r'^signup/', RegistrationView.as_view(), name = 'signup'),
    url(r'^login/', LoginView.as_view(), name = 'login'),
    url(r'profile/(?P<pk>\d+)$', UserProfileAPIView.as_view(), name='profile'),
   ]