from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.conf import settings


# custom model manager
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset()\
                                          .filter(status='published')\
                                          .order_by('-created')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'published'),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # meta information
    class Meta:
        ordering = ('-publish',) # order by publish date

    #  creating object of manager
    object = models.Manager()
    published = PublishManager() # used as custom manager

    # string representation
    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.ForeignKey('Post', related_name='post_comment', on_delete=CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    comment_body = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.OneToOneField('auth.User')
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.email
        # return self.name



