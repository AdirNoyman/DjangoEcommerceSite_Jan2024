from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True)
    brand = models.CharField(
        max_length=255, db_index=True, default='un-branded')
    slug = models.SlugField(max_length=255, db_index=True)
    # image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.PositiveIntegerField()
    # to check if product is available or not
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
