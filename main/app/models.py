from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=("Parent Category"),
    )

    parents_1 = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=("Parents Category"), related_name="sub_category"
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ("-id",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
