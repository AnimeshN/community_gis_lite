from django.urls import path
from . import views

urlpatterns = [
    path('', views.fgis, name='map')
]