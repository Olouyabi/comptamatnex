from tabnanny import verbose
from django.db import models



class MembreUser(models.Model):
    username = models.CharField(max_length=200, null=True, blank=False, verbose_name="Nom d'utilisateur")
    first_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Prénom")
    last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Prénom")
    password = models.CharField(max_length=20, null=True, blank=False, verbose_name="Mot de passe")
    shipping_id = models.CharField(max_length=20, null=True, blank=False, verbose_name="Code de livraison")
    bio = models.TextField(default="Aucun bio n'est disponible...")
    avatar = models.ImageField(upload_to='members', default='assets/imgs-blog/avatar-defualt.jpg')
    
    class Meta:
        verbose_name = 'Membre'

    def __str__(self) -> str:
        return self.username

