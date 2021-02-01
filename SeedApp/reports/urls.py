from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.reports),
    path('maps_of_trials/', views.maps_of_trials),
    path('trial_reports/', views.trial_reports),
    
]