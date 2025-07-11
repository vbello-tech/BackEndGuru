# Generated by Django 4.2.18 on 2025-05-12 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('features', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Challenge/')),
                ('difficulty', models.CharField(blank=True, choices=[('NEWBIE', 'NEWBIE'), ('JUNIOR', 'JUNIOR'), ('INTERMEDIATE', 'INTERMEDIATE'), ('ADVANCED', 'ADVANCED'), ('GURU', 'GURU')], max_length=15, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('schema_image', models.ImageField(blank=True, null=True, upload_to='Challenge/')),
                ('language', models.CharField(blank=True, max_length=150, null=True)),
                ('framework', models.CharField(blank=True, max_length=150, null=True)),
                ('database', models.CharField(blank=True, max_length=150, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('project', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('completed', models.BooleanField(default=False)),
                ('datesubmitted', models.DateTimeField(blank=True, null=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_task', to='Challenges.challenge')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
