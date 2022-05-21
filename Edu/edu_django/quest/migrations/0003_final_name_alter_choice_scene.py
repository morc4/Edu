# Generated by Django 4.0.4 on 2022-05-12 14:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0002_remove_location_slug_scene_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='final',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='scene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quest.scene'),
        ),
    ]
