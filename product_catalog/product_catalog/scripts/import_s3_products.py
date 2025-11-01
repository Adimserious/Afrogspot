from django.core.files.storage import default_storage
from product_catalog.models import Product, Category, Country
from django.utils.text import slugify
from django.utils import timezone
from datetime import timedelta

# make sure we have a category
category, _ = Category.objects.get_or_create(
    name="others",
    defaults={"friendly_name": "Others"}
)

# make sure we have a country
country, _ = Country.objects.get_or_create(
    name="Nigeria"
)

# list files in S3 under "media/"
dirs, files = default_storage.listdir('media')

created = 0

for filename in files:
    # only images
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        continue

    # make product name + sku
    name = filename.rsplit('.', 1)[0]
    sku = f"auto-{slugify(name)}"

    # don’t duplicate if we run twice
    if Product.objects.filter(sku=sku).exists():
        continue

    product = Product.objects.create(
        name=name,
        sku=sku,
        category=category,
        description=f"Auto-imported from S3 file {filename}",
        price=5.99,
        stock=10,
        image=f"media/{filename}",   # 👈 matches your S3 layout
        is_active=True,
        country=country,
        created_at=timezone.now(),
        updated_at=timezone.now(),
    )

    # mark as new arrival
    recent_threshold = timezone.now() - timedelta(days=30)
    if product.created_at >= recent_threshold:
        product.is_new_arrival = True
        product.save(update_fields=["is_new_arrival"])

    created += 1

print(f"✅ Created {created} products from S3.")

