# Generated by Django 5.1.2 on 2024-10-22 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0006_remove_comment_user_comment_utilisateur"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="films",
        ),
    ]
