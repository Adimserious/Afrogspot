from django.core.files.storage import default_storage
from product_catalog.models import Product, Category, Country
from django.utils.text import slugify
from django.utils import timezone
from datetime import timedelta

category, _ = Category.objects.get_or_create(
    name="others",
    defaults={"friendly_name": "Others"}
)

country, _ = Country.objects.get_or_create(
    name="Nigeria"
)

dirs, files = default_storage.listdir('media')
created = 0

for filename in files:
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        continue

    name = filename.rsplit('.', 1)[0]
    sku = f"auto-{slugify(name)}"

    if Product.objects.filter(sku=sku).exists():
        continue

    product = Product.objects.create(
        name=name,
        sku=sku,
        category=category,
        description=f"Auto-imported from S3 file {filename}",
        price=5.99,
        stock=10,
        image=f"media/{filename}",
        is_active=True,
        country=country,
        created_at=timezone.now(),
        updated_at=timezone.now(),
    )

    recent_threshold = timezone.now() - timedelta(days=30)
    if product.created_at >= recent_threshold:
        product.is_new_arrival = True
        product.save(update_fields=["is_new_arrival"])

    created += 1

print(f"✅ Created {created} products from S3.")

