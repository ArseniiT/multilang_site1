# main/urls.py
from django.urls import path
from .views.chatbot import chatbot, send_user_message
from .views.home import home, article_create, article_update, article_delete, article_detail_view
from .views.rag_search import search_view

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', chatbot, name='chatbot'),
    path('chatbot/send_user_message/', send_user_message, name='send_user_message'),
    path('search/', search_view, name='search'),
    path('article/new/', article_create, name='article_create'),
    path('article/<int:pk>/edit/', article_update, name='article_update'),
    path('article/<int:pk>/delete/', article_delete, name='article_delete'),
    path('article/<int:pk>/', article_detail_view, name='article_detail'),
]
