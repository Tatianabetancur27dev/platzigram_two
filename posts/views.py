from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post

# Create your views here.
@login_required
def list_posts(request):
    #dir_posts = Post.object.order_by('created')
    return render(request, "posts/feed.html")
    #{'posts': dir_posts}
