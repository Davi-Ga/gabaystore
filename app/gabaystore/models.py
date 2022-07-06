from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import MaxValueValidator
from .validators import validate_file_type, validate_file_name, validate_file_extension_and_size, validate_price, validate_quantity

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
    picture=models.ImageField(upload_to='images/',null=False,blank=False,validators=[validate_file_type,validate_file_name,validate_file_extension_and_size])
    size=models.CharField(max_length=2,null=False,choices=SIZE_CHOICES)
    clothing_type=models.CharField(max_length=20,null=False,choices=TYPES_CHOICES)
    price= models.DecimalField(max_digits=10, decimal_places=2,null=False,validators=[validate_price])
    amount=models.PositiveIntegerField(null=False,validators=[MaxValueValidator(30),validate_quantity])
    slug= models.SlugField(max_length=200, null=True, blank=True, editable=False)
    
    class Meta:
        db_table = "Cloth" 
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cloth_detail", args=[str(self.id)])
    
    
def cloth_pre_save(sender, instance, signal, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
    
signals.pre_save.connect(cloth_pre_save, sender=Cloth)