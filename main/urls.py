from django.urls import path
from .views.chatbot import chatbot
from .views.home import home


urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', chatbot, name='chatbot'),
]
