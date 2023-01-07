from django.shortcuts import render
from django.views import View
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

class BlogHome(View):
    def get(self, request, *args, **kwargs):
        all_post = Post.objects.all().order_by("-timestamp")

        p = Paginator(all_post, 15)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)

        context = {
            "all_post":all_post,
            'page_obj': page_obj
        }
        return render(request, "blog/blog.html", context)


class PostDetail(View):
    def get(self, request, SLUG, *args, **kwargs):
        post = Post.objects.get(slug=SLUG)
        context = {
            "post":post,
        }
        return render(request, "blog/blog-post.html", context)