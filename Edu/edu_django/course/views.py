from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.viewsets import ViewSet
from .models import Course, Lesson, Comment, Category, Submission, Homework
from .serializers import CourseListSerializer, CourseDetailSerializer, LessonListSerializer, CommentSerializer, CategorySerializer, QuizzSerializer, SubmissionSerializer, HomeworkSerializer

# Create your views here.
@api_view(['GET'])
def get_quiz (request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    quiz = lesson.quizzes.first()
    serializer = QuizzSerializer(quiz)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_courses(request):
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.all()

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])

    serializer = CourseListSerializer(courses, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_frontpage_courses(request):
    courses = Course.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    if request.user.is_authenticated:
        course_data = course_serializer.data
    else:
        course_data = {}


    return Response({
    'course': course_data,
    'lessons': lesson_serializer.data
    })

@api_view(['GET'])
def get_comments(request,course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request,course_slug, lesson_slug):
    data = request.data
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(course=course, lesson=lesson, name=data.get('name'), content=data.get('content'), created_by=request.user)

    serializer = CommentSerializer(comment)

    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser, JSONParser])
def add_submission(request,course_slug, lesson_slug):
    data = request.data
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    submission = Submission.objects.create(course=course, lesson=lesson, name=data.get('name'), file_submission=data.get('file_submission'), text_submission=data.get('text_submission'), created_by=request.user)

    serializer = SubmissionSerializer(submission)
    serializer.is_valid(request.data)
    serializer.save()

    return Response(serializer.data)

@parser_classes([MultiPartParser, FormParser,])
@api_view(['POST'])
def add_homework(request, course_slug, lesson_slug):
    print(request.data)
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)
    homework_file = Homework.objects.create(course=course, lesson=lesson, homework=request.data.get('homework'))
    serializer = HomeworkSerializer(data=homework_file)

    return Response(serializer.data)
