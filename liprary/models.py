from django.db import models

# Create your models here.

class Catgory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    status_book = {
        ('avilble','avilble'),
        ('rental','rental'),
        ('sold','sold'),
    }
    
    title = models.CharField(max_length=250 )
    author = models.CharField(max_length=250)
    photo_book = models.ImageField(upload_to='book', blank=True, null=True)
    photo_author = models.ImageField(upload_to='author',  blank=True, null=True)
    pages = models.IntegerField( blank=True, null=True)
    status = models.CharField(max_length=50, choices=status_book)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rental_price_day = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rental_period = models.IntegerField( blank=True, null=True)
    catgory = models.ForeignKey(Catgory, on_delete=property)
    
    def __str__(self):
        return self.title
