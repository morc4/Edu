# Generated by Django 4.0.4 on 2022-05-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_alter_lesson_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_style',
            field=models.CharField(choices=[('problem', 'problem'), ('knowledge', 'knowledge'), ('solution', 'solution'), ('task', 'task')], default='problem', max_length=20),
        ),
    ]
