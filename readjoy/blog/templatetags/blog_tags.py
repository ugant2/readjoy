


from django import template
from django.db.models import Q
from django.utils.datetime_safe import datetime
from blog.models import Post

from readjoy.settings import BLOG_NAME


register = template.Library()

# simple tag
@register.simple_tag
def blog_name():
    return BLOG_NAME

@register.simple_tag
def footer():
    year = datetime.today().year
    return "Copyright {}".format(str(year))

# Inclusion Tag
@register.inclusion_tag('blog/latest.html')
def get_latest(count=None):
    latest = []
    if count is not None:
        latest = Post.published.all()[:count]
    else:
        latest = Post.published.all()[:4]
    return {'latest_blog': latest}

# assingment tag
@register.assignment_tag
def similar(title, same_pk):
    similar = Post.published.filter(
        Q(title__contains=title) | Q(body__contains=title)
    ).exclude(pk=same_pk)
    return similar