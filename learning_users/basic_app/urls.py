from . import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerView, name='register'),
    path('login/', views.user_login, name='user_login')
]
