from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProductType(models.Model):
    # remember primary key is essentially set to autoincrement
    typename = models.CharField(max_length=255)
    typedescription = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'productype'
        verbose_name_plural = 'producttypes'


class Product(models.Model):
    productname = models.CharField(max_length=255)
    producttype = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    productprice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    productentrydate = models.DateField()
    producturl = models.URLField(null=True, blank=True)
    productdescription = models.TextField()

    def __str__(self):
        return self.productname

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'products'


class Review(models.Model):
    reviewTitle = models.CharField(max_length=255)
    reviewdate = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    reviewrating = models.SmallIntegerField()
    reviewText = models.TextField()

    def __str__(self):
        return self.reviewTitle

    class Meta:
        db_table = 'review' # if not set will include project name with table. Giving us a long String
        verbose_name_plural = 'reviews'
