from django.contrib import admin
from commande.models import*



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email',)
    search_fields = ('user',)
    ordering = ('user', )
    list_filter = ('user',)


@admin.register(VersionLivre)
class VersionLivreAdmin(admin.ModelAdmin):
    list_display = ('version', 'slug',)
    prepopulated_fields = {'slug' : ('version',)}
    search_fields = ('version',)
    ordering = ('version', )
    list_filter = ('version',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital',)
    search_fields = ('digital',)
    ordering = ('name', )
    list_filter = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered', 'complete',)
    search_fields = ('order_id', 'customer', 'date_ordered', 'complete',)
    ordering = ('date_ordered', )
    list_filter = ('date_ordered',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added',)
    search_fields = ('product', 'order', 'quantity', 'date_added',)
    ordering = ('product', )
    list_filter = ('product',)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'pays', 'ville', 'adresse', 'telephone', 'date_added',)
    search_fields = ('customer', 'pays', 'date_added',)
    ordering = ('pays', )
    list_filter = ('pays',)
