from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ()

