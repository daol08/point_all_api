from rest_framework.routers import DefaultRouter
from item.views import CategoryItemViewSet
from item import views
from django.urls import path, include

router = DefaultRouter()
router.register('', views.CategoryItemViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
