# (10/10 points) Setup a proper folder structure, use the tutorial as an example. You need a minimum of one app.

from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
