from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.viewsets import ViewSet
from .serializers import QuestSerializer, QuestManySerializer, MapSerializer, MapMapSerializer, SceneSlugSerializer, SceneSerializer, ChoicesSerializer, AnswersSerializer, AddAnswerSerializer, OutcomeSerializer, FinalSerializer
from .models import Quest, Scene, Location, Choice, Answer, Outcome, Final
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_quests(request):
    quests = Quest.objects.all()

    serializer = QuestManySerializer(quests, many=True)

    return Response(serializer.data)

@authentication_classes([])
@permission_classes([])
@api_view(['GET'])
def get_quest(request, slug):
    quest = Quest.objects.get(slug=slug)
    serializer = QuestSerializer(quest)

    return Response(serializer.data)

@api_view(['GET'])
def get_quest_map(request, slug):
    quest = Quest.objects.get(slug=slug)
    scenes = [scene.location for scene in quest.scenes.all()]
    serializer = MapSerializer(scenes, many=True)
    map_serializer = MapMapSerializer(quest)
    scene_slug = {scene.location.name: scene.slug for scene in quest.scenes.all()}
#    scene_serializer = SceneSlugSerializer(scene_slug, many=True)

    return Response({'map': map_serializer.data, 'locations': serializer.data, 'link': scene_slug})

@api_view(['GET'])
def get_scene(request, slug, scene_slug):
    scene = Scene.objects.get(slug=scene_slug)
    serializer = SceneSerializer(scene)

    return Response(serializer.data)

@api_view(['GET'])
def get_choices(request, slug, scene_slug):
    scene = Scene.objects.get(slug=scene_slug)
    options = Choice.objects.all().filter(scene=scene)
    serializer = ChoicesSerializer(options, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_answers(request, slug, scene_slug):
    scene = Scene.objects.get(slug=scene_slug)
    answers = Answer.objects.all().filter(student=request.user.id, scene=scene.id)
    serializer = AnswersSerializer(answers, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def add_answer(request, slug, scene_slug):
    data = request.data

    scene = Scene.objects.get(slug=scene_slug)
    answer_id = Choice.objects.get(text=data.get('text'))
    answer = Answer.objects.create(scene=scene, answer=answer_id, student=request.user)

    serializer = AddAnswerSerializer(answer)

    return Response(serializer.data)

@api_view(['GET'])
def calculate_score(request, slug):
#    request.user = User.objects.get(id=5) <-- for testing
    quest = Quest.objects.get(slug=slug)
    scenes = quest.scenes.all()
    score = 0

    for scene in scenes:
        answer = Answer.objects.get(student=request.user.id, scene=scene)
        score += answer.answer.score

    outcome = Outcome.objects.all().filter(quest=quest.id, student=request.user.id)

    #this view updates an existing outcome with a new score if the answers have been reseted or creates the outcome if the was no previous outcome
    if outcome.exists():
        outcome.update(accumulated_score=score)
        serializer = OutcomeSerializer(outcome, many=True)
    else:
        outcome = Outcome.objects.create(student=request.user, quest=quest, accumulated_score=score)
        serializer = OutcomeSerializer(outcome)

    return Response(serializer.data)

@api_view(['GET'])
def get_final(request, slug):
    #request.user = User.objects.get(id=5)  <-- for testing
    quest = Quest.objects.get(slug=slug)
    finals = Final.objects.all().filter(quest=quest)
    sorted = []
    for final in finals:
        sorted.append(final.needed_score)


    outcome = Outcome.objects.get(quest=quest.id, student=request.user.id)
    outcome_score = outcome.accumulated_score

    sorted.sort(reverse=True)


    def check_answer(outcome_score=outcome_score, sorted=sorted):
        if outcome_score >= sorted[0]:
            return sorted[0]
        else:
            sorted = sorted[1:]
            return check_answer(outcome_score, sorted)

    final_benchmark = check_answer()
    print(sorted)
    result = Final.objects.get(quest=quest, needed_score=final_benchmark)

    serializer = FinalSerializer(result)

    return Response(serializer.data)

@api_view(['GET'])
def been_answered(request, slug):
    quest = Quest.objects.get(slug=slug)
    scenes = quest.scenes.all()
    answers = Answer.objects.all().filter(student=request.user.id)
    if answers.count() == scenes.count():
        return Response({'answered': 1})
    else:
        return Response({'answered': 0})
