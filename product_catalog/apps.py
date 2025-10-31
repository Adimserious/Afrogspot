from django.apps import AppConfig

class ProductCatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_catalog'

    # TEMP: disable signals on Heroku so we can run migrations on empty DB
    # def ready(self):
    #     import product_catalog.signals
