from django.contrib import admin
from .models import Quest, Location, Character, Choice, Scene, Outcome, Final, Answer, Outcome
# Register your models here.
admin.site.register(Quest)
admin.site.register(Location)
admin.site.register(Character)
admin.site.register(Choice)
admin.site.register(Scene)
admin.site.register(Final)
admin.site.register(Answer)
admin.site.register(Outcome)
