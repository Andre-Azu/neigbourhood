from django.shortcuts import render,redirect
from .forms import UserSignUpForm, NeighbourHoodForm, BusinessForm, PostForm
#from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
#from django.utils.encoding import force_str,force_bytes,DjangoUnicodeDecodeError
#from django.contrib.sites.shortcuts import get_current_site
#from django.urls import reverse,reverse_lazy
#from .token_generator import account_activation_token
#from django.core.mail import EmailMessage
#from  django.http import HttpResponse,Http404
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import PasswordChangeForm
#from django.contrib.auth.views import PasswordChangeView
from nhood_app import forms
from .models import Business, NeighbourHood, Posts




# Create your views here.
@login_required(login_url='login/')
def welcome(request):
    hoods = NeighbourHood.objects.all()
    context = {
        "hoods" : hoods,
    }
    return render(request, "index.html", context)

#Usersignup view
def usersignup(request):
    form = UserSignUpForm()

    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
    
        if form.is_valid():
            
            form.save()
    else:
        
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})

# 
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        
        user = authenticate(request, password=password, username=username)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "login.html",context)
        login(request,user)
    return render(request, "login.html")

def logout(request):
    logout(request)
    return redirect('index')
    
def view_profile(request):
    context = {
        'user':request.user
    }    
    return render (request, "profile.html", context)    


# def edit_profile(request):
#     if request.method=='POST':
#         user_form=UserUpdateForm(request.POST, instance=request.user)
#         profile_form=ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return redirect('profile.html')
    # else:
    #     user_form=UserUpdateForm(instance=request.user)   
    #     profile_form=ProfileUpdateForm(instance=request.user.profile)

    # context = {
    #     "user_form":user_form,
    #     "profile_form":profile_form,
        
    # }
    # return render (request, "registration/edit_profile.html",context)  


def hood_view(request):
    if request.method == "POST":
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('welcome')
    else:
            form = NeighbourHoodForm( instance = request.user.profile)
        
    context = {
            "form":form
        }    
    return render(request,"hood.html",context)

def each_hood(request, id):
    hood = NeighbourHood.objects.get(id=id)
    
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save( commit=False)
            business.owner = request.user.profile
            business.hood =  hood
            business.save()
            return redirect('all_businesses', hood.id)
    else:
        form = BusinessForm(instance=request.user)    
    context = {
        "form" : form,
    }    
    return render(request, "business.html", context)

def all_businesses(request, id):
    
    businesses = Business.objects.filter(hood=id)
    hood = NeighbourHood.objects.get(id=id)

    
    context = {
        "businesses" : businesses,
        "hood" : hood
    }    
    return render(request, "all_businesses.html", context)



def write_post(request, id):
    
    hood = NeighbourHood.objects.get(id=id)
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save( commit=False)
            post.owner=request.user.profile
            post.hood=hood
            post.save()
            return redirect('all_posts', hood.id)
    else:
        form = PostForm(instance=request.user.profile)
    context = {
        "form" : form
    }        
    return render(request, "post.html", context)

def all_posts(request, id):
    
    hood = NeighbourHood.objects.get(id=id)
    posts = Posts.objects.filter(hood=id)
    
    context = {
        "posts" : posts,
        "hood" : hood
    }
    
    return render(request, "all_posts.html", context)

def search_hoods(request):
    
    hoods = NeighbourHood.objects.all()

    
    if 'hood' in request.GET and request.GET["hood"]:
        search_term = request.GET.get("hood")
        searched_hoods = NeighbourHood.find_neighborhood(search_term)
        message = f"{search_term}"
        
        return render(request, 'searched_hood.html', {"message":message, "searched_hoods":searched_hoods, "hoods":hoods})
    
    else:
        message ="You haven't searched for any term"
        return render(request, 'searched_hood.html',{"message":message})
   