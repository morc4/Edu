# Generated by Django 4.0.4 on 2022-05-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0004_quest_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='quest_map_picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
