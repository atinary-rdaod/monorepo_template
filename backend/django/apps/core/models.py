import uuid

from django.db import models


class BaseModel(models.Model):
    """Shared abstract model. Every domain model inherits from this.

    Single source of truth for IDs (UUID4) and audit timestamps. Add fields
    here only when they truly belong on every table.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
