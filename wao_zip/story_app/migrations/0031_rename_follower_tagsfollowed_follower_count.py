# Generated by Django 4.0.3 on 2022-09-20 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story_app', '0030_remove_tagsfollowed_followers_tagsfollowed_follower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tagsfollowed',
            old_name='follower',
            new_name='follower_count',
        ),
    ]
