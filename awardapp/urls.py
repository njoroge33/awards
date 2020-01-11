from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.signup, name='signup'),
    path('home/', views.index, name='home'),
    re_path(r'^login/', LoginView.as_view(), name='login'),
    re_path(r'^logout/', LogoutView.as_view(next_page='login'), name='logout')
]