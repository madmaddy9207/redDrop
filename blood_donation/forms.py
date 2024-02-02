# forms.py
from django import forms
from .models import RequestBlood

class RequestBloodForm(forms.ModelForm):
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Enter Name',
           'class':'form-control',
            'style':'border-radius:10px; box-shadow: 2px 2px 5px #9b9696c7;',
           
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
         'placeholder':'Enter Email',
           'class':'form-control',
            'style':'border-radius:10px; box-shadow: 2px 2px 5px #9b9696c7;',
          
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Phone Number',
           'class':'form-control',
           'style':'border-radius:10px; box-shadow: 2px 2px 5px #9b9696c7;',
           'pattern': '[0-9]{10}',
    }))
    state = forms.CharField(widget=forms.TextInput(attrs={
           'placeholder':'Enter State',
           'class':'form-control',
            'style':'border-radius:10px; box-shadow: 2px 2px 5px #9b9696c7;',
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
           'placeholder':'Enter City',
           'class':'form-control',
            'style':'border-radius:10px; box-shadow: 2px 2px 5px #9b9696c7;',
           
    }))
    address = forms.CharField(widget=forms.Textarea(attrs={
           'placeholder':'Enter Address',
           'class':'form-control ',
           'style': 'height: 56px; border: 1px solid #ccc; border-radius: 4px; border-radius:10px; box-shadow: 2px 2px 5px #9b9696c7; ',  # Add inline styles
    })) 
    date = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'Select date', 
        'class': 'form-control',
          'style':'border-radius:10px; box-shadow: 2px 2px 5px #9b9696c7;',
        }))
    BLOOD_TYPE_CHOICES = [
        ('', 'Select blood Group'),
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
    blood_group = forms.ChoiceField(
        choices=BLOOD_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control',  'style':'border-radius:10px; box-shadow: 2px 2px 5px #9b9696c7;',}),
    initial='Select blood Group'
    )
  

    class Meta:
        model = RequestBlood
        fields = ['name', 'email', 'phone', 'state', 'city', 'address', 'blood_group', 'date']

    def __init__(self, *args, **kwargs):
        super(RequestBloodForm, self).__init__(*args, **kwargs)
       
       

    def clean(self):
        cleaned_data = super().clean()
        blood_group = cleaned_data.get('blood_group')
        message = cleaned_data.get('message')

        if blood_group == 'Other' and not message:
            raise forms.ValidationError("Please provide details for 'Other' blood group.")