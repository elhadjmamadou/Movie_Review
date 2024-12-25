# Generated by Django 5.1.2 on 2024-10-20 17:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0003_critique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="critique",
            name="created_at",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="critique",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(max_length=1000)),
                ("publication", models.DateField(auto_now_add=True)),
                (
                    "critique",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie.critique",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
