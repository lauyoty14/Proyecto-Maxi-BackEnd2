from django.urls import path
from django.contrib import admin
from barberia_app.views import TurnoAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('turno/', TurnoAPI.as_view()),
]

