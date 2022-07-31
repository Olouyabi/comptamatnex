from django.shortcuts import render
from blog.models import Commentaire, Post

def home(request):
    posts = Post.published.all()
    
    context = {
        'posts' : posts,
        'navbar':'hero',
    }
    return render(request, 'pages/index.html', context)


# def contact(request):
#     return render(request, 'pages/contact.html', {'navbar':'contact',})
