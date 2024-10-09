from django.urls import path
from . import views


urlpatterns = [
    path('', views.user, name='user'),
    path('create-user/', views.create_user, name='create_user'),
    path('update-user/<int:id>/', views.update_user, name='update_user'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),
]
