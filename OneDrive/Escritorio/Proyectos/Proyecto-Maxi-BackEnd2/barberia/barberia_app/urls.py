from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^turno$', views.TurnoList.as_view()),
    re_path(r'^turno/(?P<pk>[0-9]+)$', views.TurnoDetail.as_view()),
]
