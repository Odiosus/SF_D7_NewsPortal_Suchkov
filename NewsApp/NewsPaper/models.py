# https://django.fun/docs/django/4.2/intro/tutorial02/#creating-models
import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
# модель Новость
class News(models.Model):
    article = 'AR'
    news = 'NW'
    SELECT = [(article, 'статья'), (news, 'новость')]
    # заголовок новости (уникальный заголовок исключит повторную публикацию новости)
    heading = models.CharField(max_length=150, unique=True)
    # текст новости (уникальный текст исключит повторную публикацию новости)
    text = models.TextField(unique=True)
    # поле категории ссылается на модель категории
    # все новости в категории будут доступны через поле news
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news')
    # ⚠️поле автор новости
    author = models.CharField(max_length=255)
    # https://django.fun/docs/django/4.2/intro/tutorial02/#playing-with-the-api
    pub_date = models.DateTimeField("date published: 0000-00-00 00:00:00")
    # type = models.ForeignKey(to='Type', on_delete=models.CASCADE, related_name='news')
    type = models.CharField(max_length=2, choices=SELECT)

    def __str__(self):
        return f'{self.heading.title()}: {self.text[:20]}'

    # https://django.fun/docs/django/4.2/intro/tutorial02/#playing-with-the-api
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


# Модель Категория, к которой будет привязываться новость
class Category(models.Model):
    # названия категорий уникальное
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name.title()
