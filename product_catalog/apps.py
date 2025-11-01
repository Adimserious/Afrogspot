from django.apps import AppConfig

class ProductCatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_catalog'

    # Re-enable signals now that the DB is ready
    def ready(self):
        import product_catalog.signals
