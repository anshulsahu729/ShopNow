# from django.shortcuts import render, get_object_or_404, redirect
# from .models import BlogPost
# from .forms import BlogPostForm


# def blog_list(request):
#     """Show list of active blog posts"""
#     posts = BlogPost.objects.filter(active=True).order_by('-published_date')
#     return render(request, 'blog/blog_list.html', {'posts': posts})


# def blog_detail(request, slug):
#     """Show details of a single blog post"""
#     post = get_object_or_404(BlogPost, slug=slug, active=True)
#     return render(request, 'blog/blog_detail.html', {'post': post})


# def blog_create(request):
#     """Create a new blog post"""
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_list')
#     else:
#         form = BlogPostForm()
#     return render(request, 'blog/blog_form.html', {'form': form, 'title': 'Create Blog'})


# def blog_update(request, slug):
#     """Update an existing blog post"""
#     post = get_object_or_404(BlogPost, slug=slug)
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_detail', slug=post.slug)  # ✅ fixed
#     else:
#         form = BlogPostForm(instance=post)
#     return render(request, 'blog/blog_form.html', {'form': form, 'title': 'Edit Blog'})



# def blog_delete(request, slug):
#     """Delete a blog post"""
#     post = get_object_or_404(BlogPost, slug=slug)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog_list')
#     # 👇 FIX: render blog_confirm_delete.html (not detail.html)
#     return render(request, 'blog/blog_confirm_delete.html', {'post': post})


from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost.objects.filter(active=True).order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, active=True)
    return render(request, 'blog/blog_detail.html', {'post': post})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_form.html', {'form': form, 'title': 'Create Blog'})

def blog_update(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=post.slug)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blog_form.html', {'form': form, 'title': 'Edit Blog'})

def blog_delete(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})

