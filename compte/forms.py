from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from compte.models import MembreUser
# from commande.models import ShippingAddress



class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=200, label="Nom d'utilisateur", required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 
        'id':"username", 
        'type':"text", 
        'placeholder':"Nom d'utilisateur", 
        'data-sb-validations':"required",
        'name':"username"
    }))
    first_name = forms.CharField(max_length=200, label="Prénom", required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 
        'id':"prenom", 
        'type':"text", 
        'placeholder':"Prénom", 
        'data-sb-validations':"required",
        'name':"prenom"
    }))
    last_name = forms.CharField(max_length=200, label="Nom", required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 
        'id':"nom", 
        'type':"text", 
        'placeholder':"Nom", 
        'data-sb-validations':"required",
        'name':"nom"
    }))
    email = forms.EmailField(max_length=200, label="Adresse mail", required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 
        'id':"email", 
        'type':"email", 
        'placeholder':"Adresse mail", 
        'data-sb-validations':"required",
        'name':"email"
    }))
    password = forms.CharField(max_length=200, label="Mot de passe", required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 
        'id':"password", 
        'type':"password", 
        'placeholder':"Mot de passe", 
        'data-sb-validations':"required",
        'name':"password"
    }))
    shipping_id = forms.CharField(max_length=20, label="Code de livraison", required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 
        'id':"shippingid", 
        'type':"text", 
        'placeholder':"Code de livraison", 
        'data-sb-validations':"required",
        'name':"shippingid"
    }))


    class Meta:
        model = MembreUser
        fields = ('username', 'first_name','last_name','password', 'shipping_id',)

