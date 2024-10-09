from django.urls import path
from . import views


urlpatterns = [
    path('', views.medicine, name='medicine'),
    path('create-medicine/', views.create_medicine, name='create_medicine'),
    path('update-medicine/<int:id>/', views.update_medicine, name='update_medicine'),
    path('delete-medicine/<int:id>/', views.delete_medicine, name='delete_medicine'),
    # path('<int:id>/', views.medicine_detail, name='medicine_detail'),  # Rute untuk detail obat
]