from dataclasses import fields
from xml.parsers.expat import model
from django import forms
from blog.models import Commentaire



class CommentForm(forms.ModelForm):
    commentataire = forms.CharField(max_length=100, label='nom', widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    email = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    commentaire = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows': 3}))
    
    
    class Meta:
        model = Commentaire
        fields = ['commentataire', 'email', 'commentaire']


class SearchPost(forms.Form):
    query = forms.CharField(max_length=200)


    class Meta:
        fields = ['query']