from django.db import models
from user.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)

class Tag(models.Model):
        title = models.CharField(max_length=100)

class Item(models.Model):
    categories = models.ManyToManyField(Category, related_name='items')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/item_images/')
    price = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='items')

class UserItem(models.Model):
    user = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

class History(models.Model):
    user = models.ForeignKey(User, related_name='histories', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_refunded = models.BooleanField(default=False)

class HistoryItem(models.Model):
    history = models.ForeignKey(History, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
