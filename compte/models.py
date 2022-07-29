from django.db import models
from django.contrib.auth.models import User
from commande.models import Order

class MembreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_livre = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Membre"


    def __str__(self):
        return self.code_livre.code_achat
