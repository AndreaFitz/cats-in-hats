from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choose-cat/', views.choose_cat, name='choose_cat'),
    path('choose-cat/<int:cat_id>/', views.select_cat, name='choose_cat'),
]
