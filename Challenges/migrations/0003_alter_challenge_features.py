# Generated by Django 5.0.7 on 2024-07-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Challenges', '0002_remove_challenge_instructions_challenge_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='features',
            field=models.TextField(blank=True, null=True),
        ),
    ]
