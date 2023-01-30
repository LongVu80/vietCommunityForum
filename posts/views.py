from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import PostCreateForm, ImageForm, CommentForm, ReplyForm
from .utils import update_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post, Image, Category
from .models import Comment, Reply
from django.shortcuts import reverse
from django.utils.text import slugify
from users.models import Profile


# Create your views here.
def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.latest('created')
    users = Profile.objects.all()
    context = {
        "categories": categories,
        "posts": posts,
        "latest_post": latest_post,
        "users": users,
    }
    return render(request, "posts/index.html", context)

@login_required
def post_create(request):
    if request.method == 'POST':
        # Get the post data from the request
        title = request.POST['title']
        body = request.POST['body']
        categories = request.POST.getlist('categories')
        tags = request.POST.getlist('tags')
        images = request.FILES.getlist('images')
        captions = request.POST.getlist('caption')

        # Create a new post with the given data                                 
        post = Post.objects.create(
            user=request.user,
            title=title,
            body=body
        )

        if not post.slug:
            post.slug = slugify(post.title)
            post.save()
        # Add the categories to the post
        for category in categories:
            cat = Category.objects.get(id=category)
            post.categories.add(cat)

            # Add the tags to the post
        for tag in tags:
            post.tags.add(tag)

        # Add the images to the post
        for i in range(0, len(images)):
            image = Image(post=post, images=images[i], caption=captions[i])
            image.save()
        return redirect('feed')
        # return redirect('../posts/detail', slug=post.slug)
    else:
        # Render the form template to create a new post
        categories = Category.objects.all()
        return render(request, 'posts/create.html', {'categories': categories})

def feed(request):
    # Handle form submission for creating a comment

    if request.method == 'POST':
        comment_form = CommentForm(data= request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()
         # Redirect the user back to the same page after the comment is submitted
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    posts = Post.objects.all()
    logged_user = request.user
        
    return render(request, 'posts/feed.html', {'posts': posts, 'logged_user': logged_user})



def like_post(request, id):
    post = Post.objects.get(id=id)
    if post.liked_by.filter(id=request.user.id).exists():
        # print(request.user.username)
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
        print(id, request.user.username, request.user.id)
    return redirect('detail', slug=post.slug)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'posts/category_detail.html', context)
    
def listItems(request):
    posts = Post.objects.all()
    logged_user = request.user
    return render(request, 'posts/listItems.html', {'posts': posts, 'logged_user': logged_user,})



def detail(request, id=None, slug=None):
    if request.method == 'POST':
        comment_form = CommentForm(data= request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()
        update_views(request, post)

    if id:
        post = get_object_or_404(Post, pk=id)
    elif slug:
        post = get_object_or_404(Post, slug=slug)

    logged_user = request.user
    context = {
        'post': post,
        'logged_user': logged_user,
    }
    update_views(request, post)
    return render(request, 'posts/detail.html', context)

def add_feed_reply(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        reply_text = request.POST.get('body')
        posted_by = request.POST.get('posted_by')
        reply = Reply.objects.create(comment=comment, body=reply_text, posted_by = posted_by)
        reply.save()
        print(comment_id)
    # return redirect(reverse('feed'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_reply(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        reply_text = request.POST.get('body')
        posted_by = request.POST.get('posted_by')
        reply = Reply.objects.create(comment=comment, body=reply_text, posted_by = posted_by)
        reply.save()
        return redirect('detail', slug=comment.post.slug)
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def post_view(request):
    user_id = request.GET.get('user')
    if user_id:
        posts = Post.objects.filter(user_id=user_id)
    else:
        posts = Post.objects.all()
    return render(request, 'posts/feed.html', {'posts': posts})

