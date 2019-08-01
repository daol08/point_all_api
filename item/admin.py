from django.contrib import admin
from user.models import User
from item.models import Category, Item
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)