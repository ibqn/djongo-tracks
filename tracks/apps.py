from django.apps import AppConfig


class TracksConfig(AppConfig):
    # https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
    default_auto_field = "django.db.models.AutoField"

    name = "tracks"
