from django.contrib import admin
from django.urls import path
from djangoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/',views.home, name='name'),
    path('<int:id>/', views.detail, name='detail'),
]