from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тег')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    image = models.ImageField(upload_to='posts/images/%Y/%m/%d/', verbose_name='Фото', blank=True)
    content = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False,  verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата обновления')
    views = models.IntegerField(default=0, editable=False, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Теги')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at', 'title']
