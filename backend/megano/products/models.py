from django.db import models


class ImagesModel(models.Model):
    """
        Model for avatar on product
    """
    src = models.ImageField(null=True, blank=True, upload_to='images')
    alt = models.CharField(max_length=255)

    class Meta:
        name = 'product_image'
        ordering = ['-id',]


class TagsModel(models.Model):
    """
        Model tags for product
    """
    name = models.CharField(max_length=255)

    class Meta:
        name = 'product_tags'


class SpecificationsModel(models.Model):
    """
        Model special values product
    """
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    class Meta:
        name = 'product_specifications'
        ordering = ['-id',]


class ProductModel(models.Model):
    """
        Модель продукта
    """
    images = models.ManyToManyField(ImagesModel)
    title = models.CharField(max_length=255)
    price = models.SmallIntegerField(default=0)
    count = models.SmallIntegerField(default=1)
    category = models.SmallIntegerField(default=0)
    date = models.CharField(max_length=20)
    description = models.TextField(null=False, blank=True)
    fullDescription = models.TextField(null=False, blank=True)
    freeDelivery = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    tags = models.ManyToManyField(TagsModel)
    rating = models.SmallIntegerField(default=0)
    specifications = models.ManyToManyField(SpecificationsModel)
    popular_version = models.BooleanField(default=False)
    limited_version = models.BooleanField(default=False)
    salePrice = models.SmallIntegerField(default=0)
    dateForm = models.CharField(max_length=50, null=True)
    dateTo = models.CharField(max_length=50, null=True)

    class Meta:
        name = 'product'
        ordering = ['-id',]


class ReviewModel(models.Model):
    """
        Model user review on product
    """
    product = models.ForeignKey(
        ProductModel,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    author = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    text = models.TextField(null=False, blank=True)
    rate = models.IntegerField(default=5)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        name = 'product_review'
        ordering = ['-id',]


class SubcategoriesModel(models.Model):
    """
        Product subcategories
    """
    title = models.CharField(max_length=255)
    image = models.ForeignKey(ImagesModel, on_delete=models.CASCADE)

    class Meta:
        name = 'product_subcategories'
        ordering = ['-id',]


class CategoriesModel(models.Model):
    """
        Product categories
    """
    title = models.CharField(max_length=255)
    subcategories = models.ManyToManyField(SubcategoriesModel)
    image = models.ForeignKey(ImagesModel, on_delete=models.CASCADE)

    class Meta:
        name = 'product_categories'
        ordering = ['-id',]