from django.urls import path
from mywork import views



urlpatterns = [
    path('', views.home, name='home'),
    
    
]
