from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import blogposts, images
from .forms import UploadFileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    return HttpResponse("main screen")

def blog(request):
    anonymous = "AnonymousUser"
    usernamelog = request.user
    print (usernamelog)
    blogs = blogposts.objects.all()
    return render(request, "blog/blog.html", {"blogposts": blogs, "usernamelog":usernamelog, "anonymous":anonymous})

def blogEntry(request):
    usernamelog = request.user
    postId = request.GET.get("id")
    postGet = blogposts.objects.get(id=postId)
    return render(request, "blog/blogpost.html", {"postGet": postGet, "usernamelog":usernamelog})



@login_required
def createEntry(request):
    usernamelog = request.user
    if request.method == "GET":
        return render(request, "blog/createedit.html", {"usernamelog":usernamelog})
    elif request.method == "POST":
        newp = blogposts()
        postTitle = request.POST.get("entryTitle")
        postHeadImage = request.POST.get("entryImageHeader")
        postBody = request.POST.get("postBody")
        newp.post_title = postTitle
        newp.post_image_header = postHeadImage
        newp.post_body = postBody
        newp.save()
        return render(request, "blog/createedit.html", {"post": newp})


@login_required
def resources(request):
    usernamelog = request.user
    print (usernamelog)
    if request.method == "GET":
        imagenes = images.objects.all()
        return render(request, "blog/resources.html", {"imagenes": imagenes, "usernamelog":usernamelog})
    elif request.method == "POST":
        newImg = images()
        newImg.imagefile = request.FILES["newpic"]
        newImg.save()
        imagenes = images.objects.all()
        return render(request, "blog/resources.html", {"imagenes": imagenes})

def logginview(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if next_url:
                print (request.GET.get("next"))
                print ("logged in")
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next"))
                
        else:
            return HttpResponse("<h1>Error authenticating your credentials</h1>") 
    else:
        return render(request, "blog/loggin.html")

def logoutview(request):
    logout(request)
    return HttpResponseRedirect("blog")