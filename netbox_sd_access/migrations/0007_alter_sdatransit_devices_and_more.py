# Generated by Django 5.0.7 on 2024-07-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_sd_access", "0006_merge_20240719_1535"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sdatransit",
            name="devices",
            field=models.ManyToManyField(blank=True, related_name="transit_devices", to="netbox_sd_access.sdadevice"),
        ),
        migrations.AlterField(
            model_name="sdatransit",
            name="transit_type",
            field=models.CharField(default=("lisp", "LISP", "yellow"), max_length=8),
        ),
    ]
