from django.contrib import admin
from main import models

admin.site.register(models.Beans)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.ShippingAddress)