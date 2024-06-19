from django.urls import path
from .views.chatbot import chatbot, send_user_message
from .views.home import home

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', chatbot, name='chatbot'),
    path('chatbot/send_user_message/', send_user_message, name='send_user_message'),
]
