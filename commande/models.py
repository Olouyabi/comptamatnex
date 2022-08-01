from email.mime import image
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from tomlkit import item
from comptamatnex.utilitaires import unique_order_id_generator
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here. Commande

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Utilisateur')
    name = models.CharField(max_length=200, null=True, verbose_name='nom')
    email = models.EmailField(max_length=200, null=True)

    class Meta:
        verbose_name = "Client"

    def __str__(self) :
        return self.name


class VersionLivre(models.Model):
    version = models.CharField(max_length=200, null=True, blank=False)
    slug = models.SlugField(max_length=200, null=True, blank=False)

    class Meta:
        verbose_name = "Version"

    def __str__(self):
        return self.version


class Product(models.Model):
    name = models.ForeignKey(VersionLivre, on_delete=models.CASCADE, related_name="formats_livre", verbose_name='Version')
    price = models.FloatField(verbose_name='Prix')
    description = models.TextField(null=True, blank=False)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(upload_to='formats', default='assets/commande/book-order-bg.jpg')


    def __str__(self) :
        return self.name.version

    class Meta:
        verbose_name = "Livre"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class  Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Client')
    date_ordered  = models.DateTimeField(auto_now_add=True, verbose_name='Date de la commande')
    complete = models.BooleanField(default=False, null=True, blank=False)
    order_id = models.CharField(max_length=100, blank=True, verbose_name='Code de transaction')

    class Meta:
        verbose_name = "Commande"
    
    def __str__(self) :
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

   
class OrderItem(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Livre')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Commande')
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='Quantité')
    date_added  = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Date d'ajout au panier")

    class Meta:
        verbose_name = "Article"

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Client")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Commande")
    pays = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    adresse = models.CharField(max_length=200, null=True)
    telephone = PhoneNumberField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout au panier")

    class Meta:
        verbose_name = "Adresse de livraison"
        verbose_name_plural =  "Adresse de livraison"



# def pre_save_create_order_id(sender, instance, *args, **kwargs):
#     if not instance.order_id:
#         instance.order_id = unique_order_id_generator(instance)
# pre_save.connect(pre_save_create_order_id, sender=Order)



