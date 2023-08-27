from django.contrib.auth.models import Permission
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from users.models import User
from .models import Lesson, Course, Subscription


class EducationTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='Курс',
            description='Описание курса',
            content='Содержимое курса',
            preview_image='test.png',
            owner=self.user
        )

        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course,
            is_subscribed=True
        )

    def test_create_lesson(self):
        url = reverse('education:lesson-create')
        data = {
            'title': 'Тест',
            'description': 'Тест',
            'content': 'https://www.youtube.com/',
            'course': self.course.id
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 1)
        self.assertEqual(Lesson.objects.get().title, 'Тест')

    def test_update_lesson(self):
        lesson = Lesson.objects.create(
            title='Test',
            description='Test',
            content='https://www.youtube.com/',
            course=self.course,
            owner=self.user
        )

        url = reverse('education:lesson-update', kwargs={'pk': lesson.pk})
        data = {
            'title': 'Тест',
            'description': 'Тест',
            'content': 'https://www.youtube.com/',
            'course': self.course.pk
        }

        response = self.client.put(url, data=data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['title'], data['title'])
        self.assertEquals(response.data['description'], data['description'])
        self.assertEquals(response.data['content'], data['content'])
        self.assertEquals(response.data['course'], data['course'])

    def test_create_course_subscription(self):
        """Тестирование создания подписки"""
        url = reverse('education:subscribe')
        data = {
            'course_id': self.course.id,
            'content': 'https://www.youtube.com/',
            'title': 'Тест',
            'description': 'Тест'
        }
        response = self.client.post(url, data)

        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        subscription = Subscription.objects.get(user=self.user, course=self.course)
        self.assertTrue(subscription.is_subscribed)

    def test_delete_course_subscription(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course, is_subscribed=True)
        url = reverse('education:unsubscribe', kwargs={'pk': subscription.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subscription.objects.filter(id=subscription.id).exists())
