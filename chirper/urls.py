from django.urls import path
from . import views


app_name = 'chirper'

urlpatterns = [
    path('', views.index, name='index')
]
