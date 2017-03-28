from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404


def login_page(request):
    return render(request, 'menu/login.html')


# def registration(request):

def login(request):
    if request.method == 'POST':
        print('POST data = ', request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'menu/login.html', {'username': username, 'errors': True})
    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def index(request):

    return render(request, 'index.html')


def iphone(request):

    return render(request, 'menu/iphone.html')


def htc(request):

    return render(request, 'menu/htc.html')


def blackberry(request):

    return render(request, 'menu/blackberry.html')


def samsung(request):

    return render(request, 'menu/samsung.html')


def sony(request):

    return render(request, 'menu/sony.html')


def about(request):

    return render(request, 'menu/about.html')


def xperia(request):

    return render(request, 'content/sony/xperia.html')
