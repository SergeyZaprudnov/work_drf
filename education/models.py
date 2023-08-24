from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {
    'blank': True,
    'null': True,
}


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    content = models.TextField(verbose_name='Содержимое курса', **NULLABLE)
    preview = models.ImageField(upload_to='course_previews/', verbose_name='Превью', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    content = models.TextField(verbose_name='Содержимое урока', **NULLABLE)
    preview_image = models.ImageField(upload_to='lesson_previews/', verbose_name='Превью', **NULLABLE)
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

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


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    is_subscription = models.BooleanField(default=False, verbose_name='Подписка')

    def __str__(self):
        return f'{self.user.name} - {self.course.title}'

    class Meta:
        verbose_name = 'Подписка на курс'
        verbose_name_plural = 'Подписка на курсы'
