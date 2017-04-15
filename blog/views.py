from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


'''def blog_main(requset):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'My Blogs',
    }
    return render(requset, 'blog/index.html', context)'''


def post_detail(requset, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(requset, 'blog/post_detail.html', context)


def blog_main(requset):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 2)  # show 2 instances per page

    page_request_var = 'page'
    page = requset.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)


    context = {
        'object_list': queryset,
        'title': 'List',
        'page_request_var': page_request_var
    }

    return render(requset, 'blog/index.html', context)
