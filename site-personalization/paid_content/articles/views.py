from django.shortcuts import render

from .models import Profile, Article


def show_articles(request):

    template_name = 'articles.html'
    context = dict()
    context['articles'] = Article.objects.all()

    if 'sessionid' not in request.COOKIES:
        is_new_user = True
        user_is_signed = False
    else:
        is_new_user = False
        ud = Profile.objects.get(user_session=request.COOKIES['sessionid'])
        user_is_signed = ud.signed

    context['user_is_signed'] = user_is_signed

    req = render(
        request,
        template_name,
        context,
    )

    if is_new_user:
        new_user = Profile(user_session=request.COOKIES['sessionid'])
        new_user.save()

    return req


def show_article(request, id):
    return render(
        request,
        'article.html'
    )
