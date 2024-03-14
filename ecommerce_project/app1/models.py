from django.db import models
import datetime
# Create your models here.


#Product Categories
class Ecommerce_Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Ecommerce_Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Ecommerce_Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Ecommerce_Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    # ADD SALE PRICE
    is_sale = models.BooleanField(default=False)
    sale_price =  models.DecimalField(default=0, decimal_places=2, max_digits=6)
    def __str__(self):
        return f'{self.name} {self.price}'

# Customer Orders
class Ecommerce_Order(models.Model):
    product = models.ForeignKey(Ecommerce_Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Ecommerce_Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='',blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product}'