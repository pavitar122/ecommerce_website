from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length =50)
    email= models.EmailField()
    desc= models.TextField(max_length= 100)
    phone= models.IntegerField()


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=50, default="")
    pin = models.IntegerField()
    email = models.EmailField()
    product = models.TextField()
   
