from django.shortcuts import render

from django.conf import settings
from .models import Profile, Article


def show_articles(request):

    template_name = 'articles.html'
    context = dict()
    context['articles'] = Article.objects.all()

    user_profile = Profile.objects.get_or_create(registered_user=request.user)
    context['is_signed'] = user_profile[0].signed

    req = render(
        request,
        template_name,
        context,
    )

    return req


def show_article(request, id):

    template_name = 'article.html'
    context = dict()
    context['article'] = Article.objects.get(pk=id)

    user_profile = Profile.objects.get_or_create(registered_user=request.user)
    context['is_signed'] = user_profile[0].signed

    return render(
        request,
        template_name,
        context
    )
