from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def adminpage(request):
    # Logic to retrieve data or perform actions
    # Render the admin template with necessary data
    return render(request, 'adminpage/adminpage.html')
