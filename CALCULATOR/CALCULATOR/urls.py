from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CALC_APP, name='CALC_APP'),
    path('submitquery', views.submitquery, name='submitquery'),
]
