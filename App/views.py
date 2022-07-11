from multiprocessing import context
from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import RegisterForm
from .forms import *
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

def home(request):
    blogs=Blog.objects.order_by('-created_at')
    context={
        'blogs':blogs
    }
    
    return render(request, 'home.html',context)

def blog_detail(request, slug):
    blog=Blog.objects.get(slug=slug)
    blog.views+=1
    blog.save()

    context={
        'blog':blog
    }
    return render(request, 'blog_detail.html', context)

def category_blog(request, slug):
    category=Category.objects.get(slug=slug)
    blogs=Blog.objects.filter(category=category)
    
    context={
        'blogs':blogs,
        'category':category
    }
    
    return render(request, 'home.html',context)

def tag_blog(request, slug):
    tag=Tag.objects.get(slug=slug)
    blogs=Blog.objects.filter(tags=tag)
    
    context={
        'blogs':blogs,
        'tag':tag      
    }    
    return render(request, 'home.html',context)

def category_list(request):
    return render(request, 'category_list.html')

        
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is wrong')
            return redirect('login_page')

    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('login_page')

def register(request):

    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=RegisterForm()

    context={
        'form':form,
    }
    return render(request, 'register.html', context)

@login_required(login_url='login_page')
def add_blog(request):
    form=BlogForm()
    if request.method=='POST':
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form1=form.save(commit=False)
            form1.user=request.user
            form1.slug=slugify(form1.title)
            form1.save()   
            blog=Blog.objects.get(id=form1.id)
            tags_list=form.cleaned_data['tags'] 
            tags=list(tags_list.split(',')) 
            for tag in tags:
                tag, create = Tag.objects.get_or_create(name=tag.strip())
                blog.tags.add(tag)   
            return redirect('home')
    context={
        'form':form,
    }
    return render(request, 'add_blog.html', context)


@login_required(login_url='login_page')
def update_blog(request, slug):
    blog=Blog.objects.get(slug=slug)
    context={
        'blog':blog
    }
    return render(request, 'update_blog.html', context)

@login_required(login_url='login_page')
def delete_blog(request, slug):
    blog=Blog.objects.get(slug=slug)
    context={
        'blog':blog
    }
    return render(request, 'delete_blog.html', context)