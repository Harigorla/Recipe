from django.contrib import admin
from django.urls import path

from simple_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name='index'),
]

