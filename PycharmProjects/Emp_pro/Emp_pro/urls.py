from django.contrib import admin
from django.urls import path

from Emp_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.Home)
]
