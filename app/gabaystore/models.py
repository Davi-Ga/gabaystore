from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import MaxValueValidator
from .validators import validate_file_name, validate_file_extension_and_size, validate_price, validate_quantity, validate_size, validate_clothing_type, validate_name
from django.contrib.auth.models import User

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

STATUS_CHOICES=[
        ('process','In Process'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
]

class Cloth(models.Model):
    name=models.CharField(max_length=150,null=False,unique=True,validators=[validate_name])
    picture=models.ImageField(upload_to='media/',null=False,blank=False,validators=[validate_file_name,validate_file_extension_and_size])
    size=models.CharField(max_length=2,null=False,choices=SIZE_CHOICES,validators=[validate_size])
    clothing_type=models.CharField(max_length=20,null=False,choices=TYPES_CHOICES,validators=[validate_clothing_type])
    price= models.DecimalField(max_digits=10, decimal_places=2,null=False,validators=[validate_price])
    amount=models.PositiveIntegerField(null=False,validators=[MaxValueValidator(30),validate_quantity])
    slug= models.SlugField(max_length=200, null=True, blank=True, editable=False)
    
    class Meta:
        db_table = "Cloth" 
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("gabaystore:detailClothPage", args=self.id)
    
    
def cloth_pre_save(sender, instance, signal, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
    
signals.pre_save.connect(cloth_pre_save, sender=Cloth)

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10, decimal_places=2,null=False,validators=[validate_price])
    paid_status=models.BooleanField(default=False)
    order_status=models.CharField(max_length=30,null=False,choices=STATUS_CHOICES,default='process')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "CartOrder" 
    
class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(null=False,validators=[validate_quantity])
    price=models.DecimalField(max_digits=10, decimal_places=2,null=False,validators=[validate_price])
    invoice=models.CharField(max_length=150,null=False,unique=True)
    item=models.ForeignKey(Cloth,on_delete=models.CASCADE)
    picture=models.ImageField(null=False,blank=False,validators=[validate_file_name,validate_file_extension_and_size])
    
    class Meta:
        db_table = "CartOrderItems" 
    
    def __str__(self):
        return self.cloth.name
    
    def get_absolute_url(self):
        return reverse("gabaystore:detailClothPage", args=self.cloth.id)
    
    def get_total_price(self):
        return self.quantity*self.price
    