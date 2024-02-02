
from django.urls import path
from .views import adminpage  

urlpatterns = [
    path('adminpage/', adminpage, name='adminpage'),
   
]