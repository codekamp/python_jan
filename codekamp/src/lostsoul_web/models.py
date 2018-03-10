from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User





# class User(AbstractUser):
#     bio = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class Profile(models.Model):
#     bio = models.TextField()
#     owner = models.OneToOneField()
#
#
# @receiver(models.signals.post_save, sender=User)
# def createProfile(sender, instance, created, **c):
#     if(created):
#         Profile.objects.create(user=instance)
#
# @receiver(models.signals.post_save, sender=User)
# def saveProfile(sender, instance, **c):
#     instance.profile.save()


@receiver(models.signals.pre_save, sender=Article)
def set_slug(sender, instance, **c):
    if not instance.slug:
        instance.slug = slugify(instance.title)


# https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design