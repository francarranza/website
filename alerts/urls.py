from django.conf.urls import url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'alert', api.AlertList)

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^alert/(?P<pk>[0-9]+)/$', views.AlertDetailView.as_view(), name='alert'),
    url(r'^api/', include(router.urls)),
]