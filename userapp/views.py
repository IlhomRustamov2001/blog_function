from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def users(request):
    users=User.objects.all()
    context={
        'users':users
    }

    return render(request, 'userapp/users.html', context)
