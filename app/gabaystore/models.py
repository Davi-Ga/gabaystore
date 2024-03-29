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

class Cloth(models.Model):
    name=models.CharField(max_length=150,null=True,unique=True,validators=[validate_name])
    picture=models.ImageField(upload_to='media/',null=True,blank=False,validators=[validate_file_name,validate_file_extension_and_size])
    size=models.CharField(max_length=2,null=True,choices=SIZE_CHOICES,validators=[validate_size])
    clothing_type=models.CharField(max_length=20,null=True,choices=TYPES_CHOICES,validators=[validate_clothing_type])
    price= models.DecimalField(max_digits=10, decimal_places=2,null=True)
    amount=models.PositiveIntegerField(null=True,validators=[MaxValueValidator(30)])
    slug= models.SlugField(max_length=200, null=True, blank=True, editable=False)
    users_wishlist = models.ManyToManyField(User, related_name='wishlist', blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("gabaystore:detailClothPage", args=self.id)
    
def cloth_pre_save(sender, instance, signal, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
signals.pre_save.connect(cloth_pre_save, sender=Cloth)
    
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_price=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    date_order=models.DateTimeField(auto_now_add=True,null=True)
    paid_status=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    

class OrderItem(models.Model):
    cloth=models.ForeignKey(Cloth,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity=models.PositiveIntegerField(default=0,null=True,blank=False)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.cloth.price*self.quantity
        return total
    
class Shipping(models.Model):
    customer=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address