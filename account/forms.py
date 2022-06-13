from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email adddress')
    username = forms.CharField(max_length=30, help_text="Required")
    national_id = forms.CharField(max_length=30, help_text='Required')
    phone_number = forms.CharField(max_length=30, help_text='Rewuired')
    password1 = forms.CharField(help_text='Enter password')
    password2 = forms.CharField(help_text='Enter password again')


    class Meta:
        model = Account
        fields = ("email", "username", "national_id", "phone_number", "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid credentials")