from django.db import models
from tabnanny import verbose
from django.urls import reverse

# Create your models here.
class Top_5(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название растения или насекомого')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='photos', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'Топ 5'
        verbose_name_plural = 'Топ 5'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']