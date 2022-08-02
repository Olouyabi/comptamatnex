from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from compte.models import MembreUser
# from commande.models import ShippingAddress



class RegistrationForm(forms.ModelForm):

    class Meta:
        model = MembreUser
        fields = '__all__'

