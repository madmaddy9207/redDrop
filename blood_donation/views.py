# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from .forms import RequestBloodForm
from .models import RequestBlood 



@login_required(login_url = 'login')
def request_blood(request):
    if request.method == 'POST':
       
        form = RequestBloodForm(request.POST)
       
        if form.is_valid():
            print('valid aanu')
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            blood_group = form.cleaned_data['blood_group']
            date = form.cleaned_data['date']

            # Create and save the RequestBlood object
            request_blood = RequestBlood.objects.create(
                name=name, email=email, phone=phone, state=state,
                city=city, address=address, blood_group=blood_group, date=date,
                user=request.user  # Assign the current user
            )
          
            request_blood.user = request.user
            request_blood.save()
            messages.success(request, 'Blood request submitted successfully.')
            
            return redirect('request_blood')
    else:
        form = RequestBloodForm()
        print(form.errors)
    requests = RequestBlood.objects.all()
    user_reqs = requests.filter(user=request.user)
    context = {
        'form': form,
        'requests': requests,
        'user_reqs':user_reqs,
    }

    return render(request, 'blood_donation/request_blood.html', context)




@login_required(login_url = 'login')
def edit_bloodrequest(request,id):
    
    blood_req = RequestBlood.objects.get(id=id,user_id=request.user.id)
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        blood = request.POST['blood']
        date = request.POST['date']
        
        blood_req.email = email
        blood_req.name = name
        blood_req.phone = phone
        blood_req.blood_group = blood
        blood_req.state = state
        blood_req.city = city 
        blood_req.date = date 
        blood_req.address = address
        
        blood_req.save()
        try:
            blood_req.save()
        except:
            pass
        alert = True
        return render(request, "blood_donation/edit_bloodrequest.html", {'alert':alert})
    return render(request, "blood_donation/edit_bloodrequest.html", {'blood_req':blood_req})

@login_required(login_url = 'login')
def delete_blood_request(request, request_id):
    blood_request = get_object_or_404(RequestBlood, id=request_id)

    # Check if the user has permission to delete the blood request
    if blood_request.user == request.user:
        blood_request.delete()
        messages.success(request, 'Blood request deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this blood request.')

    return redirect('request_blood')