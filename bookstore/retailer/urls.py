from django.urls import path
from . import views

app_name = 'retailer'

urlpatterns = [
    path('', views.RetailerListView.as_view(), name='retailer_list'),
    path('retailer/<int:pk>/', views.RetailerDetailView.as_view(), name='retailer_detail'),
]
