# Generated by Django 4.0.4 on 2022-05-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0003_final_name_alter_choice_scene'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
