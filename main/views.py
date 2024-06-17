from django.shortcuts import render
from .models import Article
from django.utils.translation import gettext as _


def home(request):
    welcome_message = _("Welcome to my site")
    print(welcome_message)
    return render(request, 'home.html', {'welcome_message': welcome_message})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})