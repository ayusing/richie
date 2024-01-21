# Generated by Django 3.1.7 on 2021-02-25 13:35

from django.db import migrations, models

import richie.apps.core.fields.duration


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0028_auto_20210126_2200"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="effort",
            new_name="effort_deprecated",
        ),
        migrations.AddField(
            model_name="course",
            name="effort",
            field=richie.apps.core.fields.duration.CompositeDurationField(
                blank=True,
                default_unit="hour",
                help_text="Total amount of time to complete this course.",
                max_length=80,
                null=True,
                time_units={
                    "day": ("day", "days"),
                    "hour": ("hour", "hours"),
                    "minute": ("minute", "minutes"),
                    "month": ("month", "months"),
                    "week": ("week", "weeks"),
                },
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="duration",
            field=richie.apps.core.fields.duration.CompositeDurationField(
                blank=True,
                default_unit="hour",
                help_text="The course time range.",
                max_length=80,
                null=True,
                time_units={
                    "day": ("day", "days"),
                    "hour": ("hour", "hours"),
                    "minute": ("minute", "minutes"),
                    "month": ("month", "months"),
                    "week": ("week", "weeks"),
                },
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="is_self_paced",
            field=models.BooleanField(
                default=False,
                help_text="Tick if the course pace is self paced.",
                verbose_name="is self paced",
            ),
        ),
    ]
