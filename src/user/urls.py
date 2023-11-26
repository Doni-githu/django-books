from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.Registeration.as_view())    
]
