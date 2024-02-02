import django_filters
from .models import *



class donorFilter(django_filters.FilterSet):
    class Meta:
        model = Account
        fields = '__all__'