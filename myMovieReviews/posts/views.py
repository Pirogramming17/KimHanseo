from urllib import request
from django.shortcuts import render, redirect
# Create your views here.
from .models import Post

def home(request):
    query = request.GET.get('query', None)
    if query:
        posts = Post.objects.filter(region__contains=query)
    else:
        posts = Post.objects.all()
    posts = Post.objects.all()

    print(posts)
    context = {"posts":posts}
    
    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method =="POST":
        print(request.POST)
        title = request.POST["title"]
        year = request.POST["year"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        content = request.POST["content"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        time = request.POST["time"]


        Post.objects.create(title=title, year=year, genre=genre, star=star, content=content, director=director, actor=actor, time=time)

        return redirect("/")

    context = {}
    return render(request, template_name="posts/create.html", context=context)


def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }
    return render(request, template_name="posts/detail.html", context=context)


def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        year = request.POST["year"]
        star = request.POST["star"]
        genre = request.POST["genre"]
        content = request.POST["content"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        time = request.POST["time"]

        post = Post.objects.filter(id=id).update(title=title, year=year, star=star, genre=genre, content=content, director=director, actor=actor, time=time)

        return redirect(f"/post/{id}")


    else:
        post = Post.objects.get(id=id)
        context = {
            "post": post
        }
        return render(request, template_name="posts/update.html", context=context)


def delete(request,id):
        post = Post.objects.filter(id=id)
        post.delete()
        return redirect("/")