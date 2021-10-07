from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from blog.models import Post
# posts=[
# {
# 'title':"My first post",
# 'author':"Amal",
# 'date_posted':"August 26,2021",
# 'content':"lorem ipsum ipsum lorem bla bla bla"
# },
# {
# 'title':"My second post",
# 'author':"Gokul",
# 'date_posted':"September 27,2021",
# 'content':"lorem ipsum ipsum lorem bla bla bla"
# }
# ]

# Create your views here.
def home(request):
    print('req',request)
    context = {'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about-us'})

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering=['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_list.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        print('user',user)
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # "assigning current user" by inheriting 'CreateView' class
    # having function 'form_valid'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Checking if the current user has the privilege to upadate the post
# Function inherits from the class 'UserPassesTestMixin'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
