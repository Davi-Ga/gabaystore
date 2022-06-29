from django.db import models

SIZE_CHOICES=[
    ('XS','Extra Small'),
    ('S','Small'),
    ('M','Medium'),
    ('L','Large'),
    ('XL','Extra Large')
]

TYPES_CHOICES=[
    ('T-Shirt','T-Shirt'),
    ('Hoodie','Hoodie'),
    ('Shirt','Shirt'),
]


class Cloth(models.Model):
    name=models.CharField(max_length=150,null=False,unique=True)
    picture=models.ImageField(null=False)
    size=models.CharField(max_length=2,null=False,choices=SIZE_CHOICES)
    clothing_type=models.CharField(max_length=20,null=False,choices=TYPES_CHOICES)
    
    class Meta:
        db_table = "Cloth" 
    
    def __str__(self):
        return self.name