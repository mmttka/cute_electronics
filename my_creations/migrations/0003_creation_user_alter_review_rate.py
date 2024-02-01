# Generated by Django 4.2.9 on 2024-01-31 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("my_creations", "0002_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="creation",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="review",
            name="rate",
            field=models.IntegerField(
                choices=[(3, "3"), (4, "4"), (5, "5"), (0, "0"), (2, "2"), (1, "1")]
            ),
        ),
    ]
