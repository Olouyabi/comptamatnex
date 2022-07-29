from django.contrib import admin
from . models import CategorieDePost, Post, Commentaire


# Titre du site d'administration
admin.site.site_header = "ComptaMatNex | Administration"
admin.site.site_title = "ComptaMatNex"
admin.site.index_title = "Bienvenue sur l'administration de ComptaMatNex"
# Register your models here.

@admin.register(CategorieDePost)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie', 'slug', )
    prepopulated_fields = {'slug' : ('nom_categorie',)}
    search_fields = ('nom_categorie',)
    ordering = ('nom_categorie', 'slug', )
    list_filter = ('nom_categorie', 'slug',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'status', 'date_creation', 'date_publication' ,'auteur')
    prepopulated_fields = {'slug' : ('titre',)}
    search_fields = ('titre', 'contenu',)
    ordering = ('auteur', 'status', 'date_creation',)
    list_filter = ('auteur', 'date_creation', 'date_publication',)


@admin.register(Commentaire)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'commentataire', 'email', 'creation' ,'modification')
    search_fields = ('post', 'Commentaire',)
    ordering = ('post', 'commentataire', 'creation',)
    list_filter = ('post', 'creation',)





