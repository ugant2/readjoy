from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
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


class Comment(models.Model):
    post_id = models.ForeignKey('Post', related_name='post_comment', on_delete=CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    comment_body = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=CASCADE) # this field is required
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return 'Profile of user: {}'.format(self.name.username)

    def get_absolute_url(self):
        return reverse('blogs:profile_edit', kwargs={'pk':self.pk})

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(name=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



