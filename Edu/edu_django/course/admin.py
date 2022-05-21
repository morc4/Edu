from django.contrib import admin
from .models import Category, Course, Lesson, Comment, Quiz, Submission, Homework
# Register your models here.

class LessonCommentInLine(admin.TabularInline):
    model = Comment
    raw_id_fields = ['lesson']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'status', 'lesson_type']
    list_filter = ['status', 'lesson_type']
    search_fields = ['title', 'short_description', 'long_description']
    inlines = [LessonCommentInLine]

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment)
admin.site.register(Quiz)
admin.site.register(Submission)
admin.site.register(Homework)
