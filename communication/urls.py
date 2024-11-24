from django.urls import path
from . import views

urlpatterns = [
    path('', views.communication_view, name='communication_home'),  # Home path
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),  # Delete image path
]