# Generated by Django 3.1.3 on 2020-11-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("glimpse", "0002_auto_20200915_1312"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glimpse",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inherit"),
                    ("card_square", "Square card"),
                    ("row_half", "Half row"),
                    ("row_full", "Full row"),
                    ("quote", "Quote"),
                    ("badge", "Badge"),
                ],
                default=None,
                help_text="Form factor variant",
                max_length=50,
                null=True,
                verbose_name="Variant",
            ),
        ),
    ]
