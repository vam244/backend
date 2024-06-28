from django.contrib import admin

# Register your models here.
from .models import product,cart_product


admin.site.register(product)
admin.site.register(cart_product)