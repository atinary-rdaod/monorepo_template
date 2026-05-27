from config.settings.base import *  # noqa: F403

DEBUG = False
# Run Celery tasks synchronously in unit tests — no broker required.
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
