from django.http import request
from django.shortcuts import render

from .models import Entry

# Create your views here.


def blog_view(request):
    posts = Entry.objects.all()
    blog_dict = {
        "posts": posts
    }
    return render(request, 'blog.html', blog_dict)


