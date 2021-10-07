from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        #>>> Post.objects.all()
        #>>> <QuerySet [<Post: Blog-1>]>

    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'pk':self.pk})
        # messages.success("GET",f'New post added by {self.author}')
        # return reverse('blog-home')
