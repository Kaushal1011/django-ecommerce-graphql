# Generated by Django 2.2 on 2020-06-25 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ecommerce", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="productCategory",
            new_name="product_category",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="productFullDesc",
            new_name="product_full_desc",
        ),
        migrations.RenameField(
            model_name="product", old_name="productId", new_name="product_id",
        ),
        migrations.RenameField(
            model_name="product", old_name="productName", new_name="product_name",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="productPreviewDesc",
            new_name="product_preview_desc",
        ),
        migrations.RenameField(
            model_name="product", old_name="productPrice", new_name="product_price",
        ),
        migrations.AddField(
            model_name="product",
            name="product_discount_price",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="OrderProduct",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_quantity", models.IntegerField(default=1)),
                (
                    "order_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecommerce.Product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
