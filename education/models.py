from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {
    'blank': True,
    'null': True,
}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    preview = models.ImageField(upload_to='', **NULLABLE, verbose_name='Изображение')
    description = models.CharField(max_length=150, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course', related_name='lessons')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', related_name='payments')
    date_paid = models.DateTimeField(auto_now_add=True, verbose_name='date_paid')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='lesson')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='course')
    amount = models.PositiveIntegerField(verbose_name="amount")
    type = models.CharField(max_length=30, verbose_name="type")

    def __str__(self):
        if self.lesson:
            return f'{self.user.email} paid {self.amount} for Lesson "{self.lesson.title}" via {self.type}'
        return f'{self.user.email} paid {self.amount} for Course "{self.course.title}" via {self.type}'

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        ordering = ('-date_paid',)
