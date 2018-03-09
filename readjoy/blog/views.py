from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from blog.models import Post


class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'home_list'
    queryset = Post.published.all()


class PostDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # get single PK from the post
        try:
            one_post = Post.objects.get(pk=pk)
        except:
            raise Http404()

        # context
        ctx = {
            'one_post': one_post
        }
        return render(request, template_name='blog/detail_post.html', context=ctx)


class AboutListView(ListView):
    model = Post
    template_name = 'blog/about.html'
    context_object_name = 'about_list'
    queryset = Post.published.all()
