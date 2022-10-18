from django.urls import path
from . import views

urlpatterns = [
    path('setup/', views.setup, name='setup'),
    path('predict', views.predict, name='predict'),
    path('book', views.book, name='book')
]