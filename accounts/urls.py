from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts_view, name='accounts'),
    path('register/', views.register, name='register')
]
