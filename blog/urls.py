
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('signin/',views.singIN,name='signin'),
    path('postsign/',views.postsign),
    path('logout/',views.logout,name='log'),
    path('signup/',views.singUP, name='signup'),
    path('postsignup/',views.postsignup, name='postsignup'),
    path('create/',views.create, name='create'),
    path('check/',views.check, name='check'),
]
