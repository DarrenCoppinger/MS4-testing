from django.db import models


# Create your models here.
class Product(models.Model):
    
    PINTS = 1
    BOTTLES = 2
    SOFT_DRINKS = 3
    COCKTAILS = 4
    SPIRITS = 5
    CATEGORY_CHOICES = (
        (PINTS, 'Pints'),
        (BOTTLES, 'Bottles'),
        (SOFT_DRINKS, 'Soft-drinks'),
        (COCKTAILS, 'Cocktails'),
        (SPIRITS, 'Sprints'),
    )
    category = models.SmallIntegerField(
        choices=CATEGORY_CHOICES, 
        default=PINTS)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
        

