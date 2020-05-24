from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('gtoken/', views.GenerateTokenView.as_view(), name='generate_token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
