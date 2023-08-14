from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    preview = models.ImageField(upload_to='', **NULLABLE, verbose_name='Изображение')
    description = models.CharField(max_length=150, verbose_name='Описание')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='', **NULLABLE, verbose_name='Изображение')
    description = models.CharField(max_length=150, verbose_name='Описание')
    url = models.URLField(
        default='https://my.sky.pro/student-cabinet/stream-lesson/87835/theory/5',
        verbose_name='Ссылка на видео'
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'
