from django.contrib import admin
from user.models import User
from item.models import Category, Item, Tag

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Tag)