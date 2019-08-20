
from item import views
from django.urls import path, include


urlpatterns = [
    path('<str:tag>/items/', views.TagView.as_view())
    ]