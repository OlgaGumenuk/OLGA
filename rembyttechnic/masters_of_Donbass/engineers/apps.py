from django.apps import AppConfig


class EngineersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engineers'

    def ready(self):
        import engineers.signals
