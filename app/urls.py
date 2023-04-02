from django.urls import path

from .views import Index, PostView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('post/<slug:slug>/', PostView.as_view(), name='post'),
]