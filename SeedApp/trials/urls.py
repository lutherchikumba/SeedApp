from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.home, name = 'dashboard'),
    path('trials/', views.trials, name = "trial_name"),
    path('<int:pk>/measurements/', views.measurements, name = "measurement_name"),
    path('<int:pk>/products/', views.products, name = "product_name"),
]
