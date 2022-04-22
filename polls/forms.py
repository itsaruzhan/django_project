from django import forms
from .models import Clothes, Customs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


 
class Clothesform(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}))
    info= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter info'})
    image = forms.FileField(required=False,widget= forms.FileInput(attrs={ 'class':'form-control'}))
   
    class Meta:
        model=Clothes
        fields="__all__"        

class Customsform(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}))
    info= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter info'})
    image = forms.FileField(required=False,widget= forms.FileInput(attrs={ 'class':'form-control'}))
   
    class Meta:
        model=Customs
        fields="__all__"                

class NewUserForm(UserCreationForm):
    YEARS= [x for x in range(1960,2021)]
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(required=True)
    birth_date= forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    country = CountryField().formfield()
    phoneNumber = PhoneNumberField(null = False, blank = False).formfield()

    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email","birth_date", "country", "phoneNumber","password1", "password2")
    
   