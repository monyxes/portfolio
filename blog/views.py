from django.shortcuts import render, get_object_or_404
from .models import blog

def allblogs(request):
    blogs=blog.objects
    return render(request,'allblogs.html',{'blog':blogs})
def detail(request, blog_id):
    detailed= get_object_or_404(blog, pk=blog_id)
    return render(request,'detail.html',{'blog':detailed})