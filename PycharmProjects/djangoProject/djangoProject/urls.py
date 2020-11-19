from django.contrib import admin
from django.urls import path
from djangoapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('in/',views.index),
]
