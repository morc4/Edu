from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

#unmodifyed from activity

urlpatterns = [
path('', views.get_quests),
path('<slug:slug>/get_quest/', views.get_quest),
path('<slug:slug>/get_quest_map/', views.get_quest_map),
path('<slug:slug>/<slug:scene_slug>/get_scene', views.get_scene),
path('<slug:slug>/<slug:scene_slug>/get_choices', views.get_choices),
path('<slug:slug>/<slug:scene_slug>/get_answers', views.get_answers),
path('<slug:slug>/<slug:scene_slug>/add_answer', views.add_answer),
path('<slug:slug>/calculate_score', views.calculate_score),
path('<slug:slug>/get_final', views.get_final),
path('<slug:slug>/been_answered', views.been_answered),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
