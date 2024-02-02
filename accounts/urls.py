from django.urls import path

from .views import find_donor
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
     path('find_donor/',views.find_donor, name='find_donor'),
]