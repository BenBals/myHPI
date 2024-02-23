# Generated by Django 4.2.9 on 2024-02-19 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_minutes_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taggedminutes",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_items",
                to="core.minuteslabel",
            ),
        ),
    ]