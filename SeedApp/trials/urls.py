from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('trials/', views.trials),
    path('treatments/', views.treatments),
    path('measurements/', views.measurements),
    
]