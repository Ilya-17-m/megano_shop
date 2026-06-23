from django.db import models


class ImagesModel(models.Model):
    """
        Model for avatar on product
    """
    src = models.ImageField(null=True, blank=True, upload_to='images')
    alt = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_images'
        ordering = ['-id', ]

    def __str__(self):
        return self.alt

    def __repr__(self):
        return f'<Image: alt={self.alt}>'


class TagsModel(models.Model):
    """
        Model tags for product
    """
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_tags'
        ordering = ['-id',]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Tag: name={self.name}>'


class SpecificationsModel(models.Model):
    """
        Model special values product
    """
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_specifications'
        ordering = ['-id',]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Specifications: name={self.name}, value={self.value}>'


class ProductModel(models.Model):
    """
        Модель продукта
    """
    images = models.ManyToManyField(ImagesModel)
    title = models.CharField(max_length=255)
    price = models.BigIntegerField(default=0)
    count = models.SmallIntegerField(default=1)
    category = models.ManyToManyField('CategoriesModel')
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
        db_table = 'products'
        ordering = ['-id',]

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Product: {self.title}, price={self.price}'


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
    email = models.EmailField(unique=True)
    text = models.TextField(null=False, blank=True)
    rate = models.IntegerField(default=5)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_review'
        ordering = ['-id',]

    def __str__(self):
        return self.author

    def __repr__(self):
        return f'<Review: author={self.author}, email={self.email}, text={self.text}, rate={self.rate}>'


class SubcategoriesModel(models.Model):
    """
        Product subcategories
    """
    title = models.CharField(max_length=255)
    image = models.ForeignKey(ImagesModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_subcategories'
        ordering = ['-id',]

    def __str__(self):
        return {self.title}

    def __repr__(self):
        return f'<Subcategories: title={self.title}>'


class CategoriesModel(models.Model):
    """
        Product categories
    """
    title = models.CharField(max_length=255)
    subcategories = models.ManyToManyField(SubcategoriesModel)
    image = models.ForeignKey(ImagesModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_categories'
        ordering = ['-id',]

    def __str__(self):
        return {self.title}

    def __repr__(self):
        return f'<Categories: name={self.title}>'