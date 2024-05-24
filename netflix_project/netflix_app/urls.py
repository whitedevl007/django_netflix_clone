from django.urls import path
from .views import Home


app_name = 'nextflix_app'

urlpatterns = [
    path('', Home, name='home')
]