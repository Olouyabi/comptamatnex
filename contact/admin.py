from django.contrib import admin
from contact.models import Contact



# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'objet', 'date_envoie' ,)
    search_fields = ('objet', 'date_envoie',)
    ordering = ('objet', 'date_envoie', )
    list_filter = ('objet', 'date_envoie',)