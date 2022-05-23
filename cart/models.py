from django.http import JsonResponse
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


from products.models import Product
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    items_in_cart=models.IntegerField(default=0)
    total_price=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return f"Cart has {self.items_in_cart} items of User:{self.user.username}"
    
    # def create(self):
    #     return reverse("cart:create_cart",args=[self.cart_item.name])
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="items", default=None)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)


