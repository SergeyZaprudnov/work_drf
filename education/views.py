from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from education.models import Well, Lesson
from education.serializers import WellSerializer, LessonSerializer


class WellViewSet(ModelViewSet):
    serializer_class = WellSerializer
    queryset = Well.objects.all()


class WellCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer


class WellListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class WellDetailAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class WellUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class WellDeleteAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
