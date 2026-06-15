# from django.db import models


# class Article(models.Model):
#     article_title = models.CharField("Название статьи", max_length=200)
#     article_text = models.TextField("текст статьи")
#     pub_date = models.DateTimeField("дата публикации")


# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     autors_name = models.CharField("имя автора", max_length=50)
#     comment_text = models.CharField("текст комментария", max_length=200)


# myfirst/apps/articles/models.py
from django.db import models

class MyProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    role = models.CharField(max_length=150, verbose_name="Роль / Профессия")
    bio = models.TextField(verbose_name="О себе")
    skills = models.CharField(max_length=255, help_text="Через запятую: Python, Django", verbose_name="Навыки")
    github = models.URLField(blank=True, verbose_name="Ссылка на GitHub")
    telegram = models.URLField(blank=True, verbose_name="Ссылка на Telegram")

    class Meta:
        verbose_name = "Мой профиль"
        verbose_name_plural = "Мой профиль"

    def __str__(self):
        return self.name