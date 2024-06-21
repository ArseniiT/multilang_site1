from django.shortcuts import render, redirect, get_object_or_404
from main.models import Article
from main.forms import ArticleForm
from django.views.generic import DetailView


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = ArticleForm()
    return render(request, 'article/article_form.html', {'form': form})


def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article/article_form.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('main:home')
    return render(request, 'article/article_confirm_delete.html', {'article': article})


def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'article/article_detail.html', context)

# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'article/article_detail.html'
#     context_object_name = 'article'
