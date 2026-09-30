from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import CommentForm
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Tu comentario quedó pendiente de aprobación.")
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()

    return render(
        request,
        "posts/post_detail.html",
        {"post": post, "form": form, "comments": post.comments.filter(approved=True)},
    )