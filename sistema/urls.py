from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_sistema, name='dashboard'),
    path('api/stats/', views.api_metricas_sistema, name='api_stats'),
]