# Generated by Django 3.1.7 on 2021-03-02 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
    ]

    operations = [
        migrations.CreateModel(
            name="LTIConsumer",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="lti_consumer_lticonsumer",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True,
                        help_text="For a predefined provider, leave this field empty for uploading new content.",
                        verbose_name="LTI url",
                    ),
                ),
                (
                    "lti_provider_id",
                    models.CharField(
                        blank=True,
                        choices=[("lti_provider_test", "LTI Provider Test Video")],
                        help_text="Please choose a predefined provider or fill fields below.",
                        max_length=50,
                        null=True,
                        verbose_name="Predefined LTI provider",
                    ),
                ),
                (
                    "oauth_consumer_key",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "shared_secret",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]