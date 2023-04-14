from django.shortcuts import render
from .models import Post
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView 

# Create your views here.

class PostList (ListView) : 
    model = Post

class PostDetail (DetailView) : 
    model = Post 

class PostCreate (CreateView) :
    model = Post
    fields = ['author','title','content','tags','image']
    success_url = '/blog'
    
class PostUpdate (UpdateView):
    model = Post 
    fields = ['author','title','content','tags','image']
    success_url = '/blog'

class PostDelete (DeleteView):
    model = Post 
    success_url = '/blog'

