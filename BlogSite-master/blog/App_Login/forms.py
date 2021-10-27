from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False,label="Email Address")
    phone_no = forms.CharField()
    class Meta:
        model = User
        fields = ('username','email','phone_no','password1','password2')

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name', 'password')
