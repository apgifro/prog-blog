from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('share/<int:pk>/', views.FormContactView.as_view(), name='share'),
    path('comentar/<int:pk>/', views.ComentarioCreateView.as_view(), name='comentar'),
    path('cadusuario/', views.CadUsuarioView.as_view(), name='cadusuario'),
    path('login/', views.LoginUsuarioView.as_view(), name='loginuser'),
    path('logout/', views.LogoutView.as_view(), name='logoutuser')
]
