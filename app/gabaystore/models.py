from django.db import models

SIZE_CHOICES=[
    ('XS','Extra Small'),
    ('S','Small'),
    ('M','Medium'),
    ('L','Large'),
    ('XL','Extra Large')
]

TYPES_CHOICES=[
    ('T-Shirt'),
    ('Hoodie'),
    ('Shirt'),
]


class Cloth(models.Model):
    name=models.CharField(max_length=150,null=False,unique=True)
    picture=models.ImageField()
    size=models.CharField(max_length=1,null=False,choices=SIZE_CHOICES)
    clothing_type=models.CharField(max_length=10,null=False,choices=TYPES_CHOICES)
    
    def __str__(self):
        return self.name
