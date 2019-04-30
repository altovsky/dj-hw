from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def home(request):

    template_name = 'home.html'
    context = dict()
    context['user_name'] = request.user.username

    return render(
        request,
        template_name,
        context,
    )


def signup(request):

    template_name = 'signup.html'
    context = dict()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context['form'] = form

    return render(
            request,
            template_name,
            context,
        )
