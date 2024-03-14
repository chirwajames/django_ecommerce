from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Ecommerce_Category)
admin.site.register(Ecommerce_Customer)
admin.site.register(Ecommerce_Product)
admin.site.register(Ecommerce_Order)