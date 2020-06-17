from django.urls import path
from . import views
from django.contrib.auth import views as a_views
from .views import e_insert,e_update,e_list,e_detail,e_delete

urlpatterns = [
    path('Signup',views.SignUp,name="signup"),
    path('',a_views.LoginView.as_view(template_name="rests/login.html"),name='login'),
    path('logout',a_views.LogoutView.as_view(template_name="rests/logout.html"),name='logout'),
    path('home',views.home,name='Home'),
    path('Employee',e_list.as_view(),name="Employee"),
    path('Employee/insert/',e_insert.as_view(),name="E_insert"),
    path("Employee/<pk>/update/",e_update.as_view(),name="E_update"),
    path("Employee/<pk>/",e_detail.as_view(),name="E_detail"),
     path("Employee/<pk>/delete/",e_delete.as_view(),name="E_delete")


   
]