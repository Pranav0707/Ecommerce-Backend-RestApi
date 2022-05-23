from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
PAYMENT_TYPE_CHOICES=(
    ('Cash On Delivery','Cash On Delivery'),
    ('UPI','UPI'),
    ('Card','Card')
    )

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    # stripe_token = models.CharField(max_length=100)
    payment_type=models.CharField(max_length=100,choices=PAYMENT_TYPE_CHOICES,default='Cash On Delivery')

    class Meta:
        ordering=["-created_at",]

    def __str__(self):
        return self.first_name
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_item.all())


class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name="order_item",on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name="order_item",on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    quantity=models.IntegerField(default=1)

    class Meta:
        ordering =["-id",]

    def get_cost(self):
        return self.price * self.quantity

class CouponCode(models.Model):
    coupon_code=models.CharField(max_length=100)
    is_expired=models.BooleanField(default=False)
    discounted_price=models.DecimalField(max_digits=5,decimal_places=2,default=100)
    minimum_amount=models.DecimalField(max_digits=5,decimal_places=2,default=500)

