# Generated by Django 5.0.7 on 2024-07-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_sd_access", "0012_fabricsite_comments"),
    ]

    operations = [
        migrations.AddField(
            model_name="ippool",
            name="comments",
            field=models.TextField(blank=True),
        ),
    ]