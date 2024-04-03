from django.contrib import admin
from .models import Category, Product, Size, Message, Payment, Order


admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Message)
admin.site.register(Payment)
admin.site.register(Order)
