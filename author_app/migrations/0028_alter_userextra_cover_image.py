# Generated by Django 4.0.3 on 2022-09-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author_app', '0027_alter_userextra_lists_alter_userextra_pinned_lists_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextra',
            name='cover_image',
            field=models.ImageField(default='media/author_images/profile-default.jpg', upload_to='author_images'),
        ),
    ]
