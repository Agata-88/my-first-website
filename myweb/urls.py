from django.urls import path, include
from . import views

#app_name = 'myweb'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('history/', views.history, name = 'history'),
    path('links/', views.links, name = 'links'),
    path ('shop/', views.shop, name='shop'),
    path('login/', views.login, name='login'),
    path('authenticate_user/', views.authenticate_user,
    name='authenticate_user'),
    path('show_user', views.shop, name='shop'),
    path('register', views.register, name='register')
]