from django.urls import path
from . import views

app_name = 'table_app'

urlpatterns = [
    path('', views.table_view, name='table_view'),
    path('values_endpoint/', views.values_endpoint, name='values_endpoint'),
]