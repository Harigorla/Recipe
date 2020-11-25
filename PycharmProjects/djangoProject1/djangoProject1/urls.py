from django.contrib import admin
from django.urls import path
from productApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producthome/',views.ProductHome, name='producthome'),
    path('productcreate/',views.ProductCreate, name='productcreate'),
    path('<int:id>/',views.detail, name='detail'),
]
