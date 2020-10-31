from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'William',
        'title': 'test1',
        'content': 'content test1',
        'date_posted': '2021-01-01'

    },
    {
        'author': 'wang',
        'title': 'test2',
        'content': 'content test2',
        'date_posted': '2022-01-01'

    }
]


# def home(request):
#     return HttpResponse('<h1>hello world!</h1>')


def home(request):
    context = {
        'posts': posts,
        'title': '主页'
    }
    return render(request, 'forum/home.html', context=context)


def about(request):
    return render(request, 'forum/about.html', {'title': '关于页面'})
