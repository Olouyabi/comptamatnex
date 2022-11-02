from cProfile import Profile
from tabnanny import verbose
from turtle import update
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from compte.utils import random_string_generator


class MembreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    first_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Prénom")
    last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nom")
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name="Adresse mail")
    country = models.CharField(max_length=200, blank=True, verbose_name="Pays")
    shipping_id = models.CharField(max_length=20, null=True, blank=False, verbose_name="Code de livraison")
    bio = models.TextField(default="Aucun bio n'est disponible...")
    avatar = models.ImageField(upload_to='members', default='assets/imgs-blog/avatar-default.jpg')
    friends = models.ManyToManyField(User, blank=True, related_name="friends", verbose_name="Ami")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name = 'Membre'

    def get_friends(self):
        return self.friends.all()

    def get_friends_nb(self):
        return self.friends.all().count()

    def __str__(self) -> str:
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            ex = MembreUser.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug + " " + str(random_string_generator()))
                ex = MembreUser.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


STATUS_CHOISES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(MembreUser, on_delete=models.CASCADE, related_name="sender", verbose_name="Emeteur")
    receiver = models.ForeignKey(MembreUser, on_delete=models.CASCADE, related_name="receiver", verbose_name="Recepteur")
    status = models.CharField(max_length=8, choices=STATUS_CHOISES, verbose_name="Statut")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")

    def __str__(self) -> str:
        return f"{self.sender}-{self.receiver}-{self.status}"
