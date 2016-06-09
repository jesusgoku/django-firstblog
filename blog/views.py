from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from models import Post

def home(request):
    posts = Post.objects.all()
    return render_to_response('index.html', { 'posts': posts })

class PostListView(ListView):
    model = Post
    paginate_by = 1

class PostDetailView(DetailView):
    model = Post
