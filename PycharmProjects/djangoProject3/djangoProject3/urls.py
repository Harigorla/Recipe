from django.contrib import admin
from django.urls import path
from  name_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.createpost),
]
