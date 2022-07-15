from django.urls import path, include
from . import views


app_name = "posts"

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('post/<int:id>', views.detail, name="detail"),
    path('post/<int:id>/update', views.update, name = "update"),
    path('post/<int:id>/delete', views.delete, name = "delete"),

]