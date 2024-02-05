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

    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validate/<str:uidb64>/<str:token>/',views.resetpassword_validate,name='resetpassword_validate'),
    path('resetPassword/',views.resetPassword,name='resetPassword'),
]