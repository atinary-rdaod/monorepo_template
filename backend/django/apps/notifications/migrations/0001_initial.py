import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NotificationModel",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("recipient", models.CharField(max_length=255)),
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField(blank=True, default="")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("SENT", "Sent"),
                            ("FAILED", "Failed"),
                        ],
                        default="PENDING",
                        max_length=16,
                    ),
                ),
                ("sent_at", models.DateTimeField(blank=True, null=True)),
                ("error", models.TextField(blank=True, default="")),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
