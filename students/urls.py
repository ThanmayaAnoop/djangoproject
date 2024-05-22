from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.student_create, name='student_create'),
    path('list/', views.student_list, name='student_list'),
     path('test/', views.test_template_render, name='test_template_render'),
]