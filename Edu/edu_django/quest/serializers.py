from .models import Quest, Scene, Location, Choice, Answer, Outcome, Final
from rest_framework import serializers

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'name', 'description', 'get_image')

class QuestManySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'name', 'slug')

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'get_icon')

class MapMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'get_map', 'map_name')

class SceneSlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ('id', 'slug')

class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ('id', 'get_location', 'get_character', 'intro_dialogue', 'get_character_pic')

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id','letter', 'text', 'consequence', 'score')

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'get_student', 'get_scene', 'get_answer')

class AddAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'student', 'scene', 'answer')

class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = ('id', 'student', 'quest', 'accumulated_score')

class FinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Final
        fields = ('id', 'name', 'quest', 'text', 'needed_score', 'get_picture')
