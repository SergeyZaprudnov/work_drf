from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Well(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    preview = models.ImageField(upload_to='', **NULLABLE, verbose_name='Изображение')
    description = models.CharField(max_length=150, verbose_name='Описание')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'
