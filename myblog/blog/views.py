from django.shortcuts import render
from blog.models import Article
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

# Create your views here.


# 测试的视图
def Test(request):
    # return HttpResponse('just a test!!!!')
    # articles = Article.objects.all()
    # return HttpResponse(articles[1].content)
    return render(request, 'blog/test.html', {'current_time': datetime.now()})


def home(request):
    """显示home模板"""
    art_objs = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'blog/home.html', {'post_list': art_objs, 'time': datetime.now()})


def detail(request, id):
    """显示详情页"""
    try:
        obj = Article.objects.get(id=str(id))
    except Article.DoseNotExist:
        raise Http404
    return render(request, 'blog/post.html', {'post': obj})

