
from django.urls import path
from .import views

# urlpatterns = [
#     path('', views.index, name='home'),  # Главная страница
#     path('new', views.new, name='page2'),  # Вторая страница
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),  # Новый маршрут для "Услуги"
]