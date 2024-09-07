
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('new', views.new, name='page2'),  # Вторая страница
]