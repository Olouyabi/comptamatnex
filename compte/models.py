from django.db import models
from django.contrib.auth.models import User
from commande.models import Order, Customer


class MembreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # client = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="customer")
    # email_client = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="email")
    # achat_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name="order_id")

    class Meta:
        verbose_name = "Membre"

    def __str__(self):
        return self.client
