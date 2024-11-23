from django.urls import path
from . import views

urlpatterns = [
    path('', views.communication_view, name='communication_home'),
]