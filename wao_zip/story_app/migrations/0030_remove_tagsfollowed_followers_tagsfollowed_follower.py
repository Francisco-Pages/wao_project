# Generated by Django 4.0.3 on 2022-09-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_app', '0029_remove_tagsfollowed_id_remove_tagsfollowed_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagsfollowed',
            name='followers',
        ),
        migrations.AddField(
            model_name='tagsfollowed',
            name='follower',
            field=models.BigIntegerField(default='0'),
        ),
    ]
