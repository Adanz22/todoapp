
from django.urls import path
from . import views # . => same dir

urlpatterns = [
    path('', views.index, name='index')# '' => main page
]
