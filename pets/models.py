from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Article text')
    photo = models.CharField(max_length=300, verbose_name='Photo')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time create')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Time update')
    is_published = models.BooleanField(default=True, verbose_name='Is published')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category')
    author = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-time_create', 'title']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='article')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    creat_date = models.DateTimeField(auto_now_add=True, verbose_name='comment_created')
    body = models.TextField(blank=True, verbose_name='comment_body')

    class Meta:
        ordering = ['creat_date']

    def __str__(self):
        return f'{self.body}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=250, blank=False, verbose_name='contact_name')
    email = models.EmailField(max_length=250, blank=False, verbose_name='contact_email')
    msg = models.TextField(max_length=5000, blank=False, verbose_name='contact_msg')
