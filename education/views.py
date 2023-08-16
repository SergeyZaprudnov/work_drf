from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from education.models import Course, Lesson
from education.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer


class CourseListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class CourseDetailAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class CourseUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class CourseDeleteAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
