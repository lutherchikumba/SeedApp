from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'dashboard'),
    path('trials/', views.trials, name = "trial_name"),
    path('treatments/', views.treatments, name = "treatements"),
    path('measurements/', views.measurements, name = "measurements"),
    path('products/', views.products, name = "product_name"),
    
]