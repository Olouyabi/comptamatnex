from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ViPost(models.Model):
    picture = models.ImageField(upload_to='vipost', default='', verbose_name="Image de la publication", blank=True)
    title = models.CharField(max_length=200, null=True, blank=False, verbose_name="Titre")
    body = models.TextField(verbose_name="Description")
    liked = models.ManyToManyField(User, default=None, verbose_name="Aimé", blank=True)
    # author 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Publication")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modification")

    class Meta:
        verbose_name = 'Blog VIP'
        verbose_name_plural = 'Blogs VIP'

    def __str__(self) -> str:
        return self.title

    def get_liked(self):
        return self.liked.all()

    @property
    def liked_count(self):
        return self.liked.all().count()

    def get_user_liked(self, user):
        pass
