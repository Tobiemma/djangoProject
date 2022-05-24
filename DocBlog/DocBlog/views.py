from django.http import HttpResponse
from django.shortcuts import render

from .db_articles import articles


def home_view(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home.html')


def contact_view(request):
    # return HttpResponse('Contactez-nous')
    return render(request, 'contact.html')


def article_view(request):
    return render(request, 'articles.html', context={'articles': articles})
