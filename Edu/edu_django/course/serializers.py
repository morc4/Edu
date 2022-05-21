from rest_framework import serializers

from .models import Course, Lesson, Comment, Category, Quiz, Submission, Homework

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description', 'get_image')

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'long_description')

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'slug', 'lesson_type', 'long_description', 'youtube_link')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'created_at')

class QuizzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'lesson_id', 'question', 'answer', 'option1', 'option2', 'option3')

class SubmissionSerializer(serializers.ModelSerializer):
    file_submission = serializers.FileField()
    class Meta:
        model = Submission
        fields = ('id', 'name', 'text_submission', 'created_at')

class HomeworkSerializer(serializers.ModelSerializer):
    homework = serializers.FileField()
    class Meta:
        model = Homework
        fields = ('id', 'course', 'lesson', 'homework')
