from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import employee

class Signup(UserCreationForm):
	email=forms.EmailField(required="true")


	class Meta:
		model = User
		fields= ['username','email','password1','password2']


class Employee(forms.ModelForm):

	class Meta:
		model= employee
		fields=['name','age','e_id','salary','d_no']

