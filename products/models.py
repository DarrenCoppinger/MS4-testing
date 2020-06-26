from django.db import models


# Create your models here.


class Product(models.Model):
    """ Model for drinks available """
    PINTS = 'Pints'
    BOTTLES = 'Bottles-Cans'
    SOFT_DRINKS = 'Soft-Drinks'
    COCKTAILS = 'Cocktails'
    SHORTS = 'Spirits'

    CATEGORY_CHOICES = [
        (PINTS, 'Pints'),
        (BOTTLES, 'Bottles-Cans'),
        (SOFT_DRINKS, 'Soft-Drinks'),
        (COCKTAILS, 'Cocktails'),
        (SHORTS, 'Spirits'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=PINTS,
    )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
   

    def __str__(self):
        return self.name

