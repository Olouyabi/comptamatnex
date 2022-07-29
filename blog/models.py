from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from ckeditor.fields import RichTextField
# from tinymce.models import HTMLField
from tinymce import models as tinymce_models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class CategorieDePost(models.Model):
    nom_categorie = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.nom_categorie


class Post(models.Model):
    STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published'),)
    categorie_post = models.ForeignKey(CategorieDePost, on_delete=models.CASCADE, related_name="categorie_posts")
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    contenu = tinymce_models.HTMLField()
    auteur = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posted')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now= True)
    status = models.CharField(choices=STATUS, default="draft", max_length=50)
    date_publication = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.date_publication.day, self.date_publication.month, self.date_publication.year, self.slug])


class Commentaire(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commentaires')
    commentataire = models.CharField(max_length=100, verbose_name='nom')
    email = models.EmailField(max_length=200)
    commentaire = tinymce_models.HTMLField()
    creation = models.DateTimeField(auto_now_add= True)
    modification = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.post.titre




