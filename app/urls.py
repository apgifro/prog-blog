from django.urls import path

from .views import Index, PostDetailView, FormContactView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('share/<int:pk>/', FormContactView.as_view(), name='share'),
]
