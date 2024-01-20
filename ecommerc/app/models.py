from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# CATEGORY_CHOICES = (...): Ceci définit un tuple nommé CATEGORY_CHOICES qui contient des paires clé-valeur représentant les choix possibles pour le champ category. Chaque paire consiste en un code de deux caractères et le nom associé à la catégorie.
CATEGORY_CHOICES = (
    ('ML', 'Milk'),
    ('EL', 'Elevage'),
    ('AG', 'Agricole'),
    ('AL', 'Alimentaire'),
    ('CX', 'Connexes'),
)

STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andrhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('chandigarh', 'Chandigarh'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.CharField(max_length=100, default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.IntegerField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return self.name
