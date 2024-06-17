from django.shortcuts import render
from .models import Article
from django.utils.translation import gettext as _


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)
