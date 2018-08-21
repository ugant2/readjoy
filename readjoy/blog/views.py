from email.message import EmailMessage

from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from blog.api.serializers import PostSerializer
from blog.forms import CommentForm, PostForm, ContactForm
from blog.models import Post, Profile


class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'home_list'
    paginate_by = 5
    # PAGINATOR_THEME = 'foundation'
    queryset = Post.published.all()


class PostDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')  # get single PK from the post
        try:
            one_post = Post.objects.get(
                Q(pk=pk) & Q(status='published')
            )
        except:
            raise Http404

        comment = one_post.post_comment.all()  # based on the post get comments
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


# for registering users
def register(request):
    form = None
    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            return redirect('blogs:home_pg')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


# for posting new post by the user or admin
@login_required
def new_post(request):
    form = None
    if request.method == "POST":
        new_post = PostForm(data=request.POST)
        if new_post.is_valid():
            post = new_post.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blogs:detail_pg', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/newPost.html', {'form': form})


# contact form via email
def contact_form(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        # form = contact_form(data=request.POST)
        if contact_form.is_valid():
            print("is valid form")
            email_id = request.POST.get('email_id', '')
            subject = request.POST.get('subject', '')
            email_body = request.POST.get('email_body')

            ctx = {
                'email_id': email_id,
                'subject': subject,
                'email_body': email_body,
            }
            template = get_template('email_template.html')
            email_content = template.render(context=ctx)
            email = EmailMessage(
                "Someone is tryng to contact...",
                email_content,
                'Django Blog',
                [DEFAULT_FROM_EMAIL],
                headers={'repy-to': email_id}
            )
            email.send()
            return redirect('blogs:home_pg')
        else:
            return redirect('blogs:contact_pg')
    return render(request, 'blog/contact.html', {'form': contact_form})


# for REST API
class JSONResponse(HttpResponse):
    def __init__(self, data, *args, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/JSON'
        super(JSONResponse, self).__init__(content, **kwargs)

@login_required
def post_list_api(request):
    if request.method == 'GET':
        posts = Post.published.all()
        post_serializer = PostSerializer(posts, many=True)
        return JSONResponse(post_serializer.data)

@login_required
def post_detail_api(request, pk):
    try:
        one_post = Post.published.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        post_detail_serializer = PostSerializer(one_post)
        return JSONResponse(post_detail_serializer.data)

@login_required
def api_doc(request):
    return render(request, 'blog/api_doc.html')


# for user profile
class UserProfleListView(ListView):
    model = Profile
    template_name = 'blog/profile.html'
    context_object_name = 'profile_list'

    # def update_profile(request, user_id):
    #     user = User.objects.get(pk=user_id)
    #     user.profile.name = 'Lorem'
    #     user.save()
    # Generally speaking you will never have to call the profiles save method.
    # everything is done through the User model.


class ProfileUpdateForm(UpdateView):
    model = Profile
    fields = ['name', 'email', 'address', 'phone', 'image']
    template_name = 'blog/profile_edit.html'
    # success_url = reverse_lazy('blogs:profile_pg') is needed if when get_absolute_url is not defined in model.py


class ProfileDeleteForm(DeleteView):
    model = Profile
    fields = ['name', 'email', 'address', 'phone', 'image']
    template_name = 'blog/profile_delete.html'
    success_url = reverse_lazy('blogs:home_pg')  # itll redirect to home page ater delete


# def profile_delete_view(request, pk=None):
#     obj = get_object_or_404(Profile, pk=pk)
#     if request.method == 'POST':
#         obj.delete()
#
#         return redirect('blogs:home_pg')
#     ctx = {
#         'object':obj,
#     }
#     return render(request, template_name='blog/profile_delete.html', content_type=ctx)


def profile_delete_view(request, pk):
    obj = get_object_or_404(Profile, pk=pk)
    obj.delete()
    return redirect('blogs:profile_delete')


def get_user_manual(request):
    return render(request, 'blog/user_manual.html')


def search_result(request, *args, **kwargs):
    query = request.POST.get('searchquery')
    result = Post.objects.filter(
        (Q(title__contains=query) | Q(body__contains=query)) & Q(status="published")
    )
    count = result.count()
    ctx = {
        'result': result,
        'count': count
    }

    return render(request, 'blog/search.html', context=ctx)
