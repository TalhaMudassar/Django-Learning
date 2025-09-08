from django.shortcuts import render, redirect
from blog.forms import CreatePostForm
from blog.models import Post

def home(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)  # no files, since CKEditor5 uses HTML content
        if form.is_valid():
            form.save()  # saves the Post object
            return redirect('home')  # redirect to same page after saving
    else:
        form = CreatePostForm()

    # Get all blog posts to display below the form
    blog_posts = Post.objects.all()

    return render(request, 'blog/home.html', {'form': form, 'blog_posts': blog_posts})
