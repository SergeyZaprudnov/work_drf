from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from education.models import Course, Lesson, Payment, Subscription


class LessonSerializer(ModelSerializer):
    content = serializers.CharField(validators=[validate_content])
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lesson_count = IntegerField(source='lesson_set.count', required=False)
    lessons = LessonSerializer(many=True, required=False)
    content = serializers.CharField(validators=[validate_content])
    is_subscribed = serializers.SerializerMethodField()

    @staticmethod
    def get_lessons_count(obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
