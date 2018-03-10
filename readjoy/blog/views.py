from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from blog.models import Post
from blog.forms import CommentForm


class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'home_list'
    queryset = Post.published.all()


class PostDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # get single PK from the post
        try:
            one_post = Post.object.get(
                Q(pk=pk) & Q(status='published')
            )
        except:
            raise Http404

        comment = one_post.post_comment.all() # based on the post get comments
        form_comment = CommentForm()

        # context
        ctx = {
            'post': one_post,
            'comment': comment,
            'comment_form': form_comment,
        }
        return render(request, template_name='blog/detail_post.html', context=ctx)

    # second stage is POST METHOD. POST METHOD is used to shows data in the form.
    # enables user to post comment
    def post(self, request, *args, **kwargs):
        comments = CommentForm(data=request.POST)
        if comments.is_valid():
            new_comment = comments.save(commit=False)
            post_comment = get_object_or_404(Post, pk=kwargs.get('pk'))
            new_comment.post_id = post_comment
            new_comment.save()
            return redirect('blogs:detail_pg', pk=post_comment.pk)


class AboutListView(ListView):
    model = Post
    template_name = 'blog/about.html'
    context_object_name = 'about_list'
    queryset = Post.published.all()
