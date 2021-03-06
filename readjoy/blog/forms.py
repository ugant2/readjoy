from django import forms
from blog.models import Comment, Post, Profile
from django.views.generic.edit import UpdateView


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment_body']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']


class ContactForm(forms.Form):
    email_id = forms.EmailField()
    subject = forms.CharField(max_length=50)
    email_body = forms.CharField(max_length=200, widget=forms.Textarea)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'address', 'phone', 'image']

