from django.apps import AppConfig


class Test2Config(AppConfig):
    name = 'test2'


    def ready(self):
        import test2.signals