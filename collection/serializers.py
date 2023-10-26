from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from collection.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_set.all().count()

    def get_lessons(self, course):
        return LessonSerializer(Lesson.objects.filter(course=course), many=True).data

    class Meta:
        model = Course
        fields = '__all__'
