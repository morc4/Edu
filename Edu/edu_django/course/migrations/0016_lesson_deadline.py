# Generated by Django 4.0.4 on 2022-05-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_lesson_file_submission_lesson_text_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
