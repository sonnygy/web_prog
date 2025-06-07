from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CommentForm
from .models import Comment
from django.urls import reverse
from django.contrib import messages
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.decorators.http import require_POST

def reviews(request):
    return render(request, 'myapp/reviews.html')

def initial_comments(request):
    comments = Comment.objects.all().values('id', 'name', 'text', 'rating', 'created_at')
    return JsonResponse(list(comments), safe=False)

def index(request):
    return render(request, 'myapp/index.html')

def home(request):
    return render(request, 'myapp/index__main.html')


def service(request):
    return render(request, 'myapp/service.html')


def contacts(request):
    return render(request, 'myapp/contact.html')


def reviews(request):
    comments = Comment.objects.all()
    print("reload")
    context = {
        'comments': comments,
        'rating_range': range(1, 6),
    }
    return render(request, 'myapp/reviews.html', context)


def sign_up(request):
    return render(request, 'myapp/sign-up.html')

