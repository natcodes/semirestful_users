from django.shortcuts import render
from models import *


# Create your views here.
# add an index method for views.py #if you dont do this first you will get AttributeError: 'module' object has no attribute 'index'
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'semirestapp/index.html', context)

def create(request):

    return render(request, 'semirestapp/add.html')

def show(request, id):
    context = {
        'user' : User.objects.get(id=id),
        'id': id 
    }
    return render(request, "semirestapp/show.html", context)

def update(request, id):
    context = {
        'user' : User.objects.get(id=id),
        'id': id 
    }
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.f_name = request.POST['fname']
        user.l_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()

    return render(request, 'semirestapp/edit.html', context)
#update method not working !!!
#file path issue: "update didn't match any url route" action goes to urls then to views. 
#action in form must match the urls, not views method. 

def destroy(request, id):
    User.objects.get(id=id).delete()
    return render("/")
