from django.urls import path

from . import views

app_name = 'vocab'
urlpatterns = [
    path('', views.home, name='home'),
    path('vocab/', views.index,name = 'index'),
    path('vocab/<int:vocab_id>/', views.detail , name='detail'),
    path('addPage/', views.addWordPage , name='addPage'),
    path('add/', views.addWord , name='add'),
]