from django.db import models
from musicapp.models import Account

# Create your models here.
class Product(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    product_image=models.ImageField(null=True,blank=True,upload_to='productImages')
    product_name=models.CharField(max_length=200,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        ordering=['created']



class Customer(models.Model):
    user= models.OneToOneField(Account,null=True,blank=True,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=200,null=True)
    customer_email= models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name 
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered= models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id= models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)


