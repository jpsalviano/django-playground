from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Article


class IndexView(generic.ListView):
    template_name = "articles/index.html"
    context_object_name = "latest_articles_list"
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by("-created_at")[:5]


class ReadArticleView(generic.DetailView):
    model = Article
    template_name = "articles/read.html"


class CreateArticleView(generic.CreateView):
    model = Article
    fields = ["title", "text"]
    template_name = "articles/create.html"
    
    def post(self, request):
        article = Article(title=request.POST['title'], text=request.POST['text'])
        article.save()
        return render(request, "articles/created.html")
    