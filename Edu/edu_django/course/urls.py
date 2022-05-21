from django.urls import path, include
from course import views
from quest import urls

urlpatterns = [
    path('', views.get_courses),
    path('get_frontpage_courses/', views.get_frontpage_courses),
    path('get_categories/', views.get_categories),
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments/', views.get_comments),
    path('<slug:course_slug>/<slug:lesson_slug>/get-quiz/', views.get_quiz),
    path('<slug:course_slug>/<slug:lesson_slug>/add_submission', views.add_submission),
    path('<slug:course_slug>/<slug:lesson_slug>/add_homework', views.add_homework),
    


]
