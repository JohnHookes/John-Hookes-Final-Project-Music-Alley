# Generated by Django 4.2.14 on 2024-08-12 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0002_songs_artist_name_songs_song_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='songs',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='songs',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='song_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='songs',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='songs',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='songs',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]