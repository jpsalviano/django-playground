from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Article
from .forms import ArticleForm


def index(request):
    latest_articles_list = Article.objects.order_by("-created_at")[:5]
    context = {
        "latest_articles_list": latest_articles_list,
    }
    return render(request, "articles/index.html", context)


def read_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "articles/read.html", {"article": article})


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return render(request, "articles/created.html", {"article": article})
    else:
        form = ArticleForm()
    return render(request, "articles/create.html", {"form": form})
    
    
    