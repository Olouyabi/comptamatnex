from django.contrib import admin
from compte.models import MembreUser, Relationship
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin


# Register your models here.
# class MembreUserInline(admin.StackedInline):
#     model = MembreUser
#     can_delete = False
#     verbose_name_plural = 'Vip'


# class CustomizedUserAdmin (UserAdmin):
#     inlines =  (MembreUserInline, )


# admin.site.unregister(User)
# admin.site.register(User, CustomizedUserAdmin)

admin.site.register(MembreUser)
admin.site.register(Relationship)
