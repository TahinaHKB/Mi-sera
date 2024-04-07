from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.forms import ModelForm, TextInput, PasswordInput, DateInput, EmailInput

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    prename = models.CharField(max_length=50)
    signInDate = models.DateField(default = datetime.now)
    birth = models.DateTimeField()
    email = models.CharField(max_length=1000)
    picture = models.FileField(upload_to='pictures', default='pictures/user.png')
    password = models.CharField(max_length=1000)

class MemberSignInForm(ModelForm):
    class Meta: 
        model = Member
        fields  = ['name', 'prename', 'password', 'birth', 'email']
        widgets = {
            'name' : TextInput(attrs={
                'placeholder' : 'Nom'
            }),
            'prename' : TextInput(attrs={
                'placeholder' : 'Prenom'
            }),
            'password' : PasswordInput(attrs={
                # attribut
            }),
            'birth' : DateInput(attrs={
                # attribut
            }),
            'email' : EmailInput(attrs={
                # attribut
            }),
        }

class MemberSignUpForm(ModelForm):
    class Meta: 
        model = Member
        fields  = ['email', 'password']
        widgets = {
            'email' : EmailInput(attrs={
                # attribut
            }),
            'password' : PasswordInput(attrs={
                # attribut
            }),
        }
