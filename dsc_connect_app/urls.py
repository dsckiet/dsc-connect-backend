

from dsc_connect_app.views import DscViewSet, UserViewset, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

router = DefaultRouter()
router.register(r'v1/dsc/', DscViewSet, basename='dsc')
router.register(r'v1/users/', UserViewset, basename = 'users')
urlpatterns = router.urls
urlpatterns += [
    url(r'^login/', LoginView.as_view(), name = 'login'),
    ]