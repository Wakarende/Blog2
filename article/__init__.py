from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
  name = 'article'
  label = 'article'
  verbose_name = 'Article'

  def ready(self):
    import article.signals

default_app_config = 'article.ArticlesAppConfig'

