from django.urls import path
from . import views

urlpatterns = [
    path('setup/', views.setup, name='setup'),
    path('predict', views.predict, name='predict'),
    path('book/doctor', views.book_doctor, name='book_doctor'),
    path('book/hospital', views.book_hospital, name='book_hospital'),
    path('contact', views.contact, name='contact'),
    path('predict/cervical_cancer', views.predict_cervical_cancer, name='predict_cervical_cancer'),

]