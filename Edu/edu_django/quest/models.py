from django.conf import settings
from django.db import models
from course.models import Course
from django.contrib.auth.models import User

# Create your models here.
#tentative name: Teachtory

class Quest(models.Model):
    YES = 'yes'
    NO = 'no'
    CHOICES_DELIVERABLES = ((YES,'yes'), (NO, 'no'))

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    course = models.ForeignKey(Course, related_name='quests', on_delete=models.CASCADE)
    description = models.TextField()
    has_deliverables = models.CharField(max_length=3, choices=CHOICES_DELIVERABLES, default=NO)
    picture = models.ImageField(upload_to='uploads', blank=True, null=True)
    map_name = models.CharField(max_length=50, blank=True, null=True)
    quest_map_picture = models.ImageField(upload_to='uploads', blank=True, null=True)

    def get_image(self):
        if self.picture:
            return settings.WEBSITE_URL + self.picture.url

    def get_map(self):
        if self.quest_map_picture:
            return settings.WEBSITE_URL + self.quest_map_picture.url

    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(max_length=50)
    background = models.ImageField(upload_to='uploads', blank=True, null=True)
    icon = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_background(self):
        if self.background:
            return settings.WEBSITE_URL + self.background.url

    def get_icon(self):
        if self.icon:
            return settings.WEBSITE_URL + self.icon.url

class Character(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.picture:
            return settings.WEBSITE_URL + self.picture.url

class Scene(models.Model):
    quest = models.ForeignKey(Quest, related_name='scenes', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='scenes', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, related_name='scenes', on_delete=models.CASCADE)
    intro_dialogue = models.TextField()
    name = models.CharField(max_length=50, default='quest_name', blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_character(self):
        return self.character.name

    def get_location(self):
        return self.location.name

    def get_character_pic(self):
        return settings.WEBSITE_URL + self.character.picture.url

class Choice(models.Model):
    scene = models.ForeignKey(Scene, related_name='choices', on_delete=models.CASCADE)
    letter = models.CharField(max_length=2)
    text = models.CharField(max_length=50)
    consequence = models.TextField()
    score = models.PositiveIntegerField()

    def __str__(self):
        return self.scene.location.name + " - choice: " + self.letter

class Answer(models.Model):
    scene = models.ForeignKey(Scene, related_name='answers', on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, related_name='answers', on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)

    def get_answer(self):
        return self.answer.consequence

    def get_student(self):
        return self.student.username

    def get_scene(self):
        return self.scene.slug

    def __str__(self):
        return self.scene.location.name + " - answer: " + self.answer.letter

class Outcome(models.Model):
    student = models.ForeignKey(User, related_name='outcomes', on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, related_name='outcomes', on_delete=models.CASCADE)
    accumulated_score = models.PositiveIntegerField( default=0)

    def __str__(self):
        return self.student.username+ ' - ' + self.quest.name


class Final(models.Model):
    name = models.CharField(max_length=50)
    quest = models.ForeignKey(Quest, related_name='finals', on_delete=models.CASCADE)
    text = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    needed_score = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name

    def get_picture(self):
        return settings.WEBSITE_URL + self.picture.url
