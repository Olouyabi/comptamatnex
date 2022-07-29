from django.contrib import admin
from compte.models import MembreUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class MembreUserInline(admin.StackedInline):
    model = MembreUser
    can_delete = False
    verbose_name_plural = 'Membres'


class CustomizedUserAdmin (UserAdmin):
    inlines =  (MembreUserInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(MembreUser)
