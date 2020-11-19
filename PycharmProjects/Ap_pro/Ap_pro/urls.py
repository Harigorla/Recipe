from django.contrib import admin
from django.urls import path

from Ap_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('<int:tsmodel_id>/',views.detail),
]

