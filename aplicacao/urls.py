from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),  
    path('menu/', views.menu_view, name='menu'),  
]

