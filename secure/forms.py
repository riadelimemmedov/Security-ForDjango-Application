from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Captcha
from captcha.fields import ReCaptchaField

#Crispy
from crispy_forms.helper import FormHelper#?Manipulate Html Forms with Python code
from django import forms

#Python Modules
import re

#!CreateUserForm
class CreateUserForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2','captcha']
        
    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        if not captcha:
            raise forms.ValidationError('Plese check captcha')
        return captcha

    def clean_email(self):
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists')
        elif(len(email)>320):
            raise forms.ValidationError('Your email is too long')
        elif email:
            if re.fullmatch(regex_email,email):
                print('Valid Email')
            else:
                print('Not valid email')
                raise forms.ValidationError('Please input valid email format')
        
    def __init__(self,*args,**kwargs):
        super(CreateUserForm,self).__init__(*args,**kwargs)
        for field in ['username','password1','password2']:
            self.fields[field].help_text = None
        self.helper = FormHelper()
        