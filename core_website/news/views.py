from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts, Tags, CommentToPost
from .forms import TagsForm, PostForm, CommentToPostForm


def get_tags():
    return {'all_tags': Tags.objects.all()}


def index(request):
    posts = Posts.objects.all()
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


def tag(request, name):
    t = get_object_or_404(Tags, name=name)
    posts = Posts.objects.filter(tag=t).order_by('-published_date')
    context = {'title': f'Tag {name}', 'posts': posts, 'tag': t}
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