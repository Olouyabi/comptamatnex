from multiprocessing import context
from unittest import result
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.postgres.search import SearchVector

from blog.form import CommentForm, SearchPost
from . models import CategorieDePost, Commentaire, Post


# La liste des publications
def post_list(request, category=None):
    categories = CategorieDePost.objects.all()
    posts = Post.published.all()
    if category:
        category = get_object_or_404(CategorieDePost, slug=category)
        posts = posts.filter(categorie_post=category)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'categories': categories,
        'category': category,
        'posts' : posts,
        'page' : page,
        'navbar':'blog',
    }
    return render(request, 'blog/post_list.html', context)


# Détails d'une publication
def post_detail(request, day:int, month:int, year:int, slug: str):
    categories = CategorieDePost.objects.all()
    post = get_object_or_404(Post, slug=slug, status="published", date_publication__day=day, date_publication__month=month, date_publication__year=year)
    commentaires = Commentaire.objects.filter(post=post.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Votre commentaire a été pris en compte !')
    else:
        comment_form = CommentForm()
    return render(
        request,
         'blog/post_detail.html',
          {'post' : post, 
          'categories': categories,
          'commentaires': commentaires,  
          'new_comment': new_comment, 
          'comment_form': comment_form,
          'navbar':'blog',
          })


def recherche_post(request):
    query = None
    results = []
    search_form = SearchPost()

    if 'query' in request.GET:
        search_form = SearchPost(request.GET)
        
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            results = Post.published.annotate(search=SearchVector('titre', 'contenu'),
            ).filter(search=query)

    # paginator = Paginator(results, 2)
    # page = request.GET.get('page')
    # try:
    #     results = paginator.page(page)
    # except PageNotAnInteger:
    #     results = paginator.page(1)
    # except EmptyPage:
    #     results = paginator.page(paginator.num_pages)

    context = {
        'search_form': search_form,
        'query': query,
        'results': results,
        # 'page' : page,
        'navbar':'blog',
    }

    return render(request, 'blog/recherche.html', context)