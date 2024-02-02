# forms.py
from django import forms
from .models import Account


class Registrationform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
           'placeholder':'Enter Password',
           'class':'form-control',
           'style':'background: transparent; border: 2px solid rgb(205 110 110 / 50%); outline: none; border-radius: 40px; :placeholder color: #eee1e1;'
           
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
           'placeholder':'confirm Password',
           'class':'form-control',
            'style':'background: transparent;border: 2px solid rgb(205 110 110 / 50%); outline: none; border-radius: 40px;'
            
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
           'placeholder':'Enter first Name',
           'class':'form-control-1',
            
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
           'placeholder':'Enter Last Name',
           'class':'form-control-1',
            
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
           'placeholder':'Enter Email Adrres',
           'class':'form-control-1',
            'style':'  padding: 10px 292px 11px 10px  ',
    }))
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        # Add more choices if needed
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custominput', }),
        initial='Male'  # Set the default value if needed
    )

    STATE_CHOICES = [
          ('','Select state'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Delhi', 'Delhi'),
        ('Puducherry', 'Puducherry'),
        # Add more choices if needed
    ]

    state = forms.ChoiceField(
        choices=STATE_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control custmselect', 'id': 'id_state', 
                                   'style':'background: transparent;border: 2px solid rgb(205 110 110 / 50%); outline: none; border-radius: 40px;',}),
    )
    DISTRICT_CHOICES = [
    ('', 'Select District'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Kollam', 'Kollam'),
    ('Alappuzha', 'Alappuzha'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Kottayam', 'Kottayam'),
    ('Idukki', 'Idukki'),
    ('Thrissur', 'Thrissur'),
    ('Palakkad', 'Palakkad'),
    ('Malappuram', 'Malappuram'),
    ('Kozhikode', 'Kozhikode'),
    ('Wayanad', 'Wayanad'),
    ('Kannur', 'Kannur'),
    ('Kasaragod', 'Kasaragod'),
]
    district = forms.ChoiceField(
        choices=[('', 'Select District')] + DISTRICT_CHOICES,  # Include empty and other choices
        widget=forms.Select(attrs={'class': 'form-control custmselect', 'id': 'id_district', 'style':' border: 2px solid rgb(205 110 110 / 50%); outline: none; border-radius: 40px;',}),
        required=True,  # Make the district field required
    )

    BLOOD_TYPE_CHOICES = [
         ('','Select blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
       ('Other', 'Other'),
    ]

    blood_type = forms.ChoiceField(
        choices=BLOOD_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control custmselect', 'id': 'id_blood_type', 'style':'background: transparent;border: 2px solid rgb(205 110 110 / 50%); outline: none; border-radius: 40px;',}),
        required=True,  # Make the blood type field required
    )

    other_blood_type = forms.CharField(
        max_length=50,
        required=False,  # Make the other blood type field optional initially
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_other_blood_type'}),
    )
    
    CITY_CHOICES = [
        ('', 'Select City'),
        ('City1', 'City1'),
        ('City2', 'City2'),
        ('City3', 'City3'),
        # Add more cities as needed
    ]

    city = forms.ChoiceField(choices=CITY_CHOICES,
                              widget=forms.Select(attrs={'class': 'form-control custmselect', 'style':' border: 2px solid rgb(205 110 110 / 50%); outline: none; border-radius: 40px;',}),required=False)

    is_donor = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class': 'form-check-input','style':'margin-left: 10px;'}),)

    class Meta:
          model = Account
          fields = ['first_name','last_name', 'gender', 'state', 'district','email','password','is_donor']

def clean(self):
    cleaned_data = super(Registrationform, self).clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    if password != confirm_password:
        raise forms.ValidationError("Password does not match!!")

                       
    #exit from the meta class
    #and this is for call css for all form attrib or elements 
    
def __init__ (self, *args, **kwargs):
         super(Registrationform, self).__init__(*args,**kwargs)
        
         self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
         self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number '
         self.fields['address'].widget.attrs['placeholder'] = 'Enter address '
         self.fields['dob'].widget.attrs['placeholder'] = 'Enter dob '
         self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
         for field in self.fields:
              self.fields[field].widget.attrs['class']='form-control'

