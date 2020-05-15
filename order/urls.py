from django.urls import path
from . import views


urlpatterns = [
    path('menu',views.menus,name="menu"),
    path('',views.order,name='order'),
    ]