# Generated by Django 4.0.3 on 2022-07-04 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('story_app', '0002_rename_author_story_author_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_date', models.DateField(default=django.utils.timezone.now)),
                ('liker_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('story_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='story_app.story')),
            ],
        ),
    ]
