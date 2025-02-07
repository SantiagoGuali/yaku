from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name="home"),
    path('Dashboards', views.viewDashboards, name="Dashboards"),
    
]
