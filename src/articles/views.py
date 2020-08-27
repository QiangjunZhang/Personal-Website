from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .forms import ArticleForm
from .models import Article


# Create your views here.
def index(request):
    articles_list = Article.objects.order_by('id')
    context = {
        'articles_list': articles_list,
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})


def article_create_view(request):
    return render(request, "articles/create_article.html")


def article_save_view(request):
    new_article = Article()
    new_article.title = request.POST['title']
    new_article.content = request.POST['content']
    new_article.pub_date = timezone.now()
    new_article.save()
    return HttpResponseRedirect(reverse('articles:detail', args=(new_article.id,)))


def article_delete_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return HttpResponseRedirect(reverse('articles:index'))
