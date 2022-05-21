from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Categories'

class Course(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url

        else:
            return 'http://bulma.io/images/placeholders/1280x960.png'

class Lesson(models.Model):
    DRAFT ='draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
    (DRAFT, 'draft'),
    (PUBLISHED, 'published')
    )

    PROBLEM = 'problem'
    KNOWLEDGE = 'knowledge'
    SOLUTION = 'solution'
    TASK ='task'

    CHOICES_LESSON_STYLE = (
    (PROBLEM, 'problem'),
    (KNOWLEDGE, 'knowledge foundation'),
    (SOLUTION, 'solution'),
    (TASK, 'task')
    )

    ARTICLE = 'article'
    QUIZ = 'quiz'
    VIDEO = 'video'
    SUBMISSION = 'submission'

    CHOICES_LESSON_TYPE = (
    (ARTICLE, 'article'), (QUIZ, 'quiz'), (VIDEO, 'video'), (SUBMISSION, 'submission'),
    )

    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    lesson_style = models.CharField(max_length=20, choices=CHOICES_LESSON_STYLE, default=PROBLEM)
    lesson_type = models.CharField(max_length=20, choices=CHOICES_LESSON_TYPE, default=ARTICLE)
    youtube_link = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=PUBLISHED)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.title

class Submission(models.Model):
    course = models.ForeignKey(Course, related_name='submissions', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='submissions', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text_submission = models.TextField(blank=True, null=True)
    file_submission =  models.FileField(upload_to='uploads', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson.title + ' - ' + self.name

    def get_file(self):
        if self.file_submission:
            return settings.WEBSITE_URL + self.file_submission.url




class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='quizzes', on_delete=models.CASCADE)
#    course = self.lesson.course
    question = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    option3 = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.lesson.title + ' - ' + self.lesson.course.title

class Homework(models.Model):
    course = models.ForeignKey(Course, related_name='homework', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='homework', on_delete=models.CASCADE)
    homework =  models.FileField(upload_to='uploads', blank=True, null=True)
    def __str__(self):
        return self.lesson.title
