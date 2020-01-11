from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.signup, name='signup'),
    path('home/', views.index, name='home'),
    re_path(r'^login/', LoginView.as_view(), name='login')
]