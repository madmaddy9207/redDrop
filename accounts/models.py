from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Create your models here.

#this is super admin
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('user must have an username')
        
        user = self.model(
            #the normilizeemail means that if we enter Caps letter email is automatically normlize that
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name,last_name,username,email,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user





class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    username   = models.CharField(max_length=50,unique=True)
    email      = models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=50)
    gender      = models.CharField(max_length=50)
    state      = models.CharField(max_length=50)
    district   = models.CharField(max_length=50, blank=True)
    blood_type   = models.CharField(max_length=50)
    city   = models.CharField(max_length=50)
    address   = models.CharField(max_length=50)
    dob   = models.CharField(max_length=10, blank=True)


    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    objects = MyAccountManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.is_donor = False
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.email
    
    #this is for if the user is admin they have the permission to change all the thinks
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
   