from django.db import models #Cela importe la classe models du module django.db, qui est utilisée pour définir les modèles dans Django.

# Create your models here.

# CATEGORY_CHOICES = (...): Ceci définit un tuple nommé CATEGORY_CHOICES qui contient des paires clé-valeur représentant les choix possibles pour le champ category. Chaque paire consiste en un code de deux caractères et le nom associé à la catégorie.
CATEGORY_CHOICES = (
    ('ML', 'Milk'),
    ('EL', 'Elevage'),
    ('AG', 'Agricole'),
    ('AL', 'Alimentaire'),
    ('CX', 'Connexes'),
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
