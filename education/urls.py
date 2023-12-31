from django.urls import path
from rest_framework import routers

from education.apps import EducationConfig
from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonDetailAPIView, \
    LessonUpdateAPIView, LessonDeleteAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = EducationConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
                  path('subscribe/', SubscriptionCreateAPIView.as_view(), name='subscribe'),
                  path('subscribe/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='unsubscribe'),
              ] + router.urls
