from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Blogss
from django.core.paginator import Paginator , EmptyPage , InvalidPage

# Create your views here.
def index(request):
    categories = Category.objects.all()
    blogs=Blogss.objects.all()
    latest = Blogss.objects.all().order_by('-pk')[:4]

    paginator = Paginator(blogs,3)
    try:
        page = int(request.GET.get('page','1'))
    except :
        page = 1
    
    try :
        blogPerpage = paginator.page(page)
    except (EmptyPage,InvalidPage):
        blogPerpage = paginator.page(paginator.num_pages)

    return render(request,"frontend/index.html", {
        'categories':categories,
        'blogs':blogPerpage,
        'latest':latest
    })


def blogDetail(request,id):
    categories = Category.objects.all()
    popular = Blogss.objects.all().order_by('-views')[:3]
    suggestion = Blogss.objects.all().order_by('views')[:3]
    singleBlog = Blogss.objects.get(id=id)
    singleBlog.views = singleBlog.views+1
    singleBlog.save()
    return render(request,"frontend/blogDetail.html",{"blog":singleBlog,'categories':categories,'popular':popular,'suggestion':suggestion})