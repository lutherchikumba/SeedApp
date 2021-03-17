from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'dashboard'),
    path('trials/', views.trials, name = "trial_name"),
    path('measurements/', views.measurements, name = "measurements"),
    path('<int:pk>/products/', views.products, name = "product_name"),
    
]