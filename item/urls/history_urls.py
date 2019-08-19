from rest_framework.routers import DefaultRouter
from item.views import HistoryViewSet
from item import views
from django.urls import path, include

router = DefaultRouter()
router.register('', views.HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
