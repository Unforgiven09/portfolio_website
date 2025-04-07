from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts, Tags, CommentToPost
from .forms import TagsForm, PostForm, CommentToPostForm


def get_tags():
    recent_posts = Posts.objects.order_by('-published_date')[:50]
    recent_tags = Tags.objects.filter(posts__in=recent_posts).annotate(num_posts=Count('posts')
    ).order_by('-num_posts')[:10]
    return {'all_tags': Tags.objects.all(), 'recent_tags': recent_tags}


def index(request):
    posts = Posts.objects.filter(is_published=True)
    context = {
        'title': 'News',
        'posts': posts,
    }
    context.update(get_tags())
    return render(request, 'news/index.html', context)


def post(request, post_slug):
    post_obj = get_object_or_404(Posts, slug=post_slug)
    comments = CommentToPost.objects.filter(post=post_obj)

    if request.method == 'POST':
        form = CommentToPostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post_obj
            comment.save()
            return redirect('post', post_slug=post_obj.slug)
    else:
        form = CommentToPostForm()

    context = {
        'title': f'Post {post_obj}',
        'post': post_obj,
        'add_comment': form,
        'comments': comments,
    }
    context.update(get_tags())
    return render(request, "news/post.html", context)


def tag(request, tag_slug):
    t = get_object_or_404(Tags, slug=tag_slug)
    posts = Posts.objects.filter(tag=t, is_published=True).order_by('-published_date')
    context = {'title': f'Tag {tag_slug}', 'posts': posts, 'tag': t}
    context.update(get_tags())
    return render(request, "news/tag.html", context)


def all_tag(request,):
    context = {'title': 'All tags',}
    context.update(get_tags())
    return render(request, "news/all_tags.html", context)


@login_required
def add_news(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = PostForm()
    context = {'title': 'Add news','form': form}
    context.update(get_tags())
    return render(request, "news/add_news.html", context)


@login_required
def add_tags(request):
    if request.method == 'POST':
        form = TagsForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = TagsForm()
    context = {'title': 'Add tags', 'form': form}
    context.update(get_tags())
    return render(request, "news/add_tags.html", context)


@login_required
def change_post(request, slug):
    post_to_change = get_object_or_404(Posts, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post_to_change)
        if form.is_valid():
            form.save()
            return redirect('post', post_slug=post_to_change.slug)
    else:
        form = PostForm(instance=post_to_change)
    context = {'title': 'Add news','form': form}
    context.update(get_tags())
    return render(request, "news/change_post.html", context)


def find_author(request, author):
    user = User.objects.get(username=author)
    posts = Posts.objects.filter(user=user)
    context = {
        'title': f'News by author {author}',
        'posts': posts,
    }
    context.update(get_tags())
    return render(request, 'news/index.html', context)


def search(request):
    query = request.GET.get('query')
    posts = Posts.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {'title': f'News by search: {query}',
               'posts': posts}
    context.update(get_tags())
    return render(request, "news/index.html", context)