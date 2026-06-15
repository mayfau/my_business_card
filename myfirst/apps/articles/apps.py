# myfirst/apps/articles/apps.py
from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myfirst.apps.articles'
    label = 'myfirst_articles'
