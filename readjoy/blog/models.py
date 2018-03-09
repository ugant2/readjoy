from django.db import models
from django.utils import timezone


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


