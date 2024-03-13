from django.db import models


# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2550)
    description = models.TextField()

    def __str__(self):
        return self.name

from django.contrib.auth.models import User
class Customer1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default='NA')

    def str(self):
        return self.user.username


class Cartitem(models.Model):
    customer = models.ForeignKey(Customer1, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    coffee = models.ForeignKey(Coffee,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'cart_items'

    def __str__(self):
        return self.coffee.name 

class ShippingAddress1(models.Model):
    customer=models.ForeignKey(Customer1,on_delete=models.CASCADE,null=True)
    building_name=models.CharField(max_length=300,null=False,blank=False)
    street=models.CharField(max_length=200,blank=True)
    landmark=models.CharField(max_length=200,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=30,null=False)
    zipcode=models.CharField(max_length=8,null=False)
    date_added=models.DateTimeField(auto_now_add=True)










