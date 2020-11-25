from django.contrib import admin
from django.urls import path


from Recipe_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('<int:id>/details',views.details),
    path('',views.results),
    path('',views.recipe),
]
