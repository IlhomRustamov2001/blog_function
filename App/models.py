from unicodedata import category
from django import views
from django.db import models
from django.contrib.auth.models import User
from platformdirs import user_runtime_dir 
class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    image= models.ImageField(upload_to='category/%Y/%m/%d')
    blog_count=models.IntegerField(default=0)
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.name

    

class Blog(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50, unique=True)
    content=models.TextField()
    image=models.ImageField(upload_to='blog/%Y/%m/%d')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    views=models.IntegerField(default=0)
    tags=models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'

class Tag(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200, unique=True)

    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save(*args, **kwargs)
    
class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text