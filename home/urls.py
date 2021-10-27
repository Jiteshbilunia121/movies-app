from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('sort/<str:slug>/', views.sort, name='sort'),

    path('detail/<int:id>/', views.detail, name='detail'),
    path('play/<int:id>/', views.play, name='play'),

    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
