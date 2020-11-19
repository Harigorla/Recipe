from django.contrib import admin
from django.urls import path
from Recipe_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/',views.RecipeView),
    path('home/',views.Home),
    path('detail/',views.details),
    path('result',views.results),
]


