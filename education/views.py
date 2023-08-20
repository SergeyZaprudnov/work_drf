from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from education.models import Course, Lesson, Payment
from education.permissions import CoursePermission, LessonPermission
from education.serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from users.models import UserRoles


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, CoursePermission]

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)
        new_course.owner = self.request.user
        new_course.save()

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user).order_by('id')


class CourseCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [AllowAny, LessonPermission]

    def perform_create(self, serializer):
        new_lesson = serializer.save(owner=self.request.user)
        new_lesson.owner = self.request.user
        new_lesson.save()


class CourseListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != UserRoles.MODERATOR:
            queryset = Lesson.objects.filter(owner=self.request.user)
        else:
            queryset = Lesson.objects.all()
        return queryset


class CourseDetailAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny, LessonPermission]

    def get_queryset(self):
        return Lesson.objects.all()


class CourseUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, LessonPermission]

    def get_queryset(self):
        return Lesson.objects.all()


class CourseDeleteAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny, LessonPermission]


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ('date_paid',)
    filterset_fields = ('course', 'lesson', 'type',)
    permission_classes = [IsAuthenticated]
