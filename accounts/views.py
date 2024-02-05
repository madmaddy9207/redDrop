from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Account
from .forms import Registrationform
from .filters import donorFilter

#verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            state = form.cleaned_data['state']
            blood_type = form.cleaned_data['blood_type']
            district = form.cleaned_data['district']
            city = form.cleaned_data['city']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            is_donor = form.cleaned_data.get('is_donor', False)
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            
            user.gender = gender
            user.blood_type = blood_type
            user.city = city
            user.district =district
            user.state =state
            user.is_donor = is_donor
            user.save()

            #user Activation
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verifiaction_email.html', {
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()

            # messages.success(request, 'Registration Successful')

            return redirect('/accounts/login/?command=verification&email='+email)

    else:
        form = Registrationform()

    context = {
        'form': form,
    }
     
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, email=email, password=password)
   

        if user is not None:
            auth.login(request, user)
            print("loggin success")
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out ')
    return redirect('login')

@login_required(login_url = 'login')
def profile(request):
    donor_profile = Account.objects.get(username=request.user.username)
    return render(request, "profile/profile.html", {'donor_profile':donor_profile})

@login_required(login_url = 'login')
def edit_profile(request):
    donor_profile = Account.objects.get(username=request.user.username)
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        blood = request.POST['blood']
        date = request.POST['date']
       

        donor_profile.email = email
        donor_profile.first_name = first_name
        donor_profile.last_name = last_name
        donor_profile.phone_number = phone
        donor_profile.blood_type = blood
        donor_profile.state = state
        donor_profile.city = city 
        donor_profile.dob = date 
        donor_profile.address = address
        
        is_donor = request.POST.get('is_donor', False)
        donor_profile.is_donor = is_donor == 'on'

        donor_profile.save()
 
        try:
            donor_profile.save()
        except:
            pass
        alert = True
        return render(request, "profile/edit_profile.html", {'alert':alert})
    return render(request, "profile/edit_profile.html", {'donor_profile':donor_profile})




@login_required(login_url='login')
def find_donor(request):
    if request.method=='POST':                   
        selected_state = request.POST.get("state", "")
        print(selected_state)
        selected_district = request.POST.get("district", "")
        print(selected_district)
        selected_blood_type = request.POST.get("blood_type", "")
        print(selected_blood_type)

        donors = Account.objects.all()  
    
        
        if selected_state:
            donors = donors.filter(state__iexact=selected_state)  # Case-insensitive filter
            
        if selected_district:
            donors = donors.filter(district__iexact=selected_district)
        
        if selected_blood_type:
            donors = donors.filter(blood_type__iexact=selected_blood_type)
        

        if not donors.exists():
            message = "No blood donors available in selected location and blood type."
            
        else:
            message = ""  # No message when results found
            print('4')
        context = {"donors": donors, "message": message}
        return render(request, 'accounts/find_donor.html', context)
    else:
        return render(request, 'accounts/find_donor.html')




def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Congratulations! Your account is activated.')
        else:
            messages.error(request, 'Invalid activation link')
            return redirect('register')
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        messages.error(request, 'Invalid activation link')
        return redirect('register')

    # Return a redirect response or any other appropriate response
    return redirect('login')  # Redirect to login page after activation


# def forgotPassword(requset):
#     if requset.method == 'POST':
#         email = requset.POST['email']
#         if Account.objects.filter(email=email).exists():
#             user=Account.objects.get(email__exact=email)

#             # reset password email
#             current_site = get_current_site(request)
#             mail_subject = 'Reset Your Password'
#             message = render_to_string('accounts/reset_password_email.html', {
#                 'user' : user,
#                 'domain' : current_site,
#                 'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token' : default_token_generator.make_token(user)
#             })
#             to_email = email
#             send_email = EmailMessage(mail_subject,message,to=[to_email])
#             send_email.send()

#             messages.success(requset,'Password Reset email has been send to Your email address.')
#             return redirect('login')

#         else:
#             messages.error(requset,'Account does not exists')
#             return redirect('forgotPassword')

#     return render(requset,'accounts/forgotPassword.html')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Use get method to avoid KeyError
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')

        else:
            messages.error(request, 'Account does not exist')
            return redirect('forgotPassword')

    return render(request, 'accounts/forgotPassword.html')




def resetpassword_validate(request, uidb64, token):
      try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

      except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
       user=None

      if user is not None and default_token_generator.check_token(user, token):
          request.session['uid'] = uid
          messages.success(request,'Please reset your Password')
          return redirect('resetPassword')
      else:
          messages.error(request,'This link has been expired')
          return redirect('login')
      

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,'Password rest successful')
            return redirect('login')
        else:
            messages.error(request,'Password do not match!')
            return redirect('resetPassword')
    else:
      return render(request,'accounts/resetPassword.html')