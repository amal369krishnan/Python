from django.urls import path
from . import views
from .views import PostListView,UserPostListView,PostDetailView,PostDeleteView,PostCreateView,PostUpdateView

urlpatterns = [
# path('', views.home,name="blog-home"),
path('', PostListView.as_view(),name="blog-home"),
path('user/<str:username>/', UserPostListView.as_view(),name="blog-user-post"),
path('detail/<int:pk>/', PostDetailView.as_view(), name="blog-post-detail"),
path('post/create/',PostCreateView.as_view(),name = "blog-create"),
path('detail/<int:pk>/update/', PostUpdateView.as_view(), name="blog-post-update"),
path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-post-delete"),
path('about/',views.about,name="blog-about")
]
