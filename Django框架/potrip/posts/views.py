from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post
import requests

# Create your views here.
'''
def index(request):
    posts = Post.objects.all() #相當於SELECT * FROM posts_post
    #posts = Post.objects.filter(location="台南") #相當於SELECT * FROM posts_post WHERE location="台南"
    #posts = Post.objects.get(id=1) #相當於SELECT * FROM posts_post WHERE id=1

    return render(request, "posts/index.html", {"posts": posts})
'''

def index(request):
    response = requests.get(
        "https://emma.pixnet.cc/mainpage/blog/categories/hot/28") #線上公開資料
    articles = response.json()["articles"] #轉換為JSON物件後，存取articles欄位
    return render(request, "posts/index.html", {"articles": articles})