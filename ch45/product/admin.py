from django.contrib import admin
from product.models import Product
class ProductModelAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["id", "name", "description", "price"]

# Now register the new UserModelAdmin
admin.site.register(Product, ProductModelAdmin)
