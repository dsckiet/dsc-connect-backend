from django.urls import path
from dsc_connect_app import views
from .views import DscList, DscDetail, api_root, custom404

urlpatterns = [
	path('v1/dsc/<int:pk>/',DscDetail.as_view()),
	path('v1/dsc/', DscList.as_view()),
	path('', views.api_root, name = 'dsc-list'),
	#path('', views.api_root),
]

handler404 = custom404