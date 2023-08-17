from django.urls import path
from rest_framework import routers

from education.apps import EducationConfig
from education.views import CourseViewSet, CourseCreateAPIView, CourseListAPIView, CourseDetailAPIView, \
    CourseUpdateAPIView, CourseDeleteAPIView, PaymentListAPIView

app_name = EducationConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', CourseCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', CourseListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', CourseDetailAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', CourseDeleteAPIView.as_view(), name='lesson_delete'),

    path('payments/', PaymentListAPIView.as_view(), name='payments-list')
] + router.urls
