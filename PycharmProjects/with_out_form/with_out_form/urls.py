from django.contrib import admin
from django.urls import path
from with_out_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.Wview)
]
