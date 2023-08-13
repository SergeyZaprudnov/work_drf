from django.urls import path
from rest_framework import routers

from education.apps import EducationConfig
from education.views import WellViewSet, WellListAPIView, WellCreateAPIView, WellDetailAPIView, WellUpdateAPIView, \
    WellDeleteAPIView

app_name = EducationConfig.name

router = routers.DefaultRouter()
router.register(r'well', WellViewSet, basename='well')

urlpatterns = [
    path('lesson/create/', WellCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', WellListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', WellDetailAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', WellUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', WellDeleteAPIView.as_view(), name='lesson_delete'),
] + router.urls
