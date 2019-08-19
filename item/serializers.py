from rest_framework import serializers
from .models import Item, UserItem, Category, HistoryItem, History, CategoryItem



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']



class ItemSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Item
        fields =['id', 'title', 'description', 'created', 'price', 'image', 'category',  'category_id']

class CategoryItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    category = CategorySerializer()
    class Meta:
        model = CategoryItem
        fields = ['category', 'item']



class UserItemSerializer(serializers.ModelSerializer):

    item = ItemSerializer()

    class Meta:
        model = UserItem
        fields = ['item', 'user', 'count']

class HistoryItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = HistoryItem
        fields = ['history', 'item', 'count']

class HistorySerializer(serializers.ModelSerializer):
    items = HistoryItemSerializer(many=True)
    class Meta:
        model = History
        fields = ['id','user', 'created', 'is_refunded', 'items']

