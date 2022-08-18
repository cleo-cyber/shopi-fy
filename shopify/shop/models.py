from django.db import models

# Create your models here.
class Product(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    product_image=models.ImageField(null=True,blank=True,upload_to='productImages')
    price=models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        ordering=['created']