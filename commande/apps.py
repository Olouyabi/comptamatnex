from django.apps import AppConfig


class CommandeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commande'

    def ready(self):
        import commande.signals