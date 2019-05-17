from django.shortcuts import render

from django.conf import settings
from .models import Profile, Article


def show_articles(request):

    template_name = 'articles.html'
    current_session = request.session
    current_session.save()
    # user_key = request.session.session_key

    context = dict()
    context['articles'] = Article.objects.all()

    # user_profile = Profile.objects.get_or_create(user_session=user_key)
    user_profile = Profile.objects.get_or_create(registered_user=request.user)
    context['is_signed'] = user_profile[0].signed

    # context['site_path'] = f"http://{request.META['HTTP_HOST']}{request.META['PATH_INFO']}"

    req = render(
        request,
        template_name,
        context,
    )

    return req


def show_article(request, id):

    template_name = 'article.html'
    current_session = request.session
    current_session.save()
    user_key = request.session.session_key

    context = dict()
    context['article'] = Article.objects.get(pk=id)

    # user_profile = Profile.objects.get_or_create(user_session=user_key)
    user_profile = Profile.objects.get_or_create(registered_user=request.user)
    context['is_signed'] = user_profile[0].signed

    return render(
        request,
        template_name,
        context
    )
