# Generated by Django 4.0.4 on 2022-05-30 09:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import walets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Wallet",
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
                (
                    "name",
                    models.CharField(
                        default=walets.models.Wallet.wallet_name_generator,
                        editable=False,
                        max_length=8,
                        unique=True,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("visa", "Visa"),
                            ("mastercard", "Mastercard"),
                        ],
                        default="Visa",
                        max_length=10,
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("EUR", "EUR"),
                            ("USD", "USD"),
                            ("RUB", "RUB"),
                        ],
                        default="EUR",
                        max_length=3,
                    ),
                ),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        editable=False,
                        max_digits=10,
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                (
                    "modified_on",
                    models.DateTimeField(auto_now=True, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]