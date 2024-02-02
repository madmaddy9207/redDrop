# blood_donation/urls.py
from django.urls import path
from .views import delete_blood_request, edit_bloodrequest, request_blood

urlpatterns = [
    path('request_blood/', request_blood, name='request_blood'),
    path('edit_bloodrequest/<int:id>/', edit_bloodrequest, name='edit_bloodrequest'),
     path('delete/<int:request_id>/', delete_blood_request, name='delete_blood_request'),
    
    # Add other URL patterns as needed
]
