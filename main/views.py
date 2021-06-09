from django.shortcuts import render
from django.template.defaulttags import register
from .models import Posts


def index(request):
    post_info = Posts.objects.all()
    return render(request, 'main/index.html', {'post': post_info})