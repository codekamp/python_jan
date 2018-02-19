from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    # def save(self, *a, **b):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #
    #     super(Article, self).save(a, b)




class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


@receiver(models.signals.pre_save, sender=Article)
def set_slug(sender, instance, **c):
    if not instance.slug:
        instance.slug = slugify(instance.title)

