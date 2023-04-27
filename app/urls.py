from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('share/<int:pk>/', views.FormContactView.as_view(), name='share'),
    path('comentar/<int:pk>/', views.ComentarioCreateView.as_view(), name='comentar'),
]
