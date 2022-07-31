from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=200, null=False, blank=False)
    prenom = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    objet = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField()
    date_envoie = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.objet
