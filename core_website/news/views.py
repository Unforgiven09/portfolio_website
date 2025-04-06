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


def post(request, title):
    post_obj = get_object_or_404(Posts, slug=title)
    comments = CommentToPost.objects.filter(post=post_obj)

    if request.method == 'POST':
        form = CommentToPostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post_obj
            comment.save()
            return redirect('post', title=post_obj.slug)
    else:
        form = CommentToPostForm()

    context = {
        'post': post_obj,
        'add_comment': form,
        'comments': comments,
    }
    context.update(get_tags())
    return render(request, "news/post.html", context)


def tag(request, name):
    t = get_object_or_404(Tags, name=name)
    posts = Posts.objects.filter(tag=t).order_by('-published_date')
    context = {'posts': posts, 'tag': t}
    context.update(get_tags())
    return render(request, "news/tag.html", context)

def all_tag(request,):
    context = {}
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
    context = {'form': form}
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
    context = {'form': form}
    context.update(get_tags())
    return render(request, "news/add_tags.html", context)