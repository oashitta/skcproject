from django.apps import AppConfig


class MyPagesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_pages_app'
def ready(self):
        import my_pages_app.signals

