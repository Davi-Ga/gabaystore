from django.core.exceptions import ValidationError
import os
import re

BLACKLIST=['name','picture','size','clothing_type','price','amount','slug','id','created_at','updated_at','__str__','get_absolute_url','__unicode__','__repr__']    
    
def validate_file_name(image):
    filename = image.file.name
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise ValidationError('Unsupported file extension.')
    else:
        return image

def validate_file_extension_and_size(image):
    ext = os.path.splitext(image.file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    filesize = image.file.size
    if filesize > 2097152:
        raise ValidationError('File too large. Size limit is 2 MB.')
    else:
        return image

def validate_price(value):
    if value < 0:
        raise ValidationError('Price cannot be negative.')
    if value == 0:
        raise ValidationError('Price cannot be zero.')
    else:
        return value
    
def validate_quantity(value):
    if value < 0:
        raise ValidationError('Quantity cannot be negative.')
    if value == 0:
        raise ValidationError('Quantity cannot be zero.')
    else:
        return value
    
def validate_size(value):
    if value not in ['XS','S','M','L','XL']:
        raise ValidationError('Size must be one of the following: XS, S, M, L, XL')
    else:
        return value
    
def validate_clothing_type(value):
    if value not in ['T-Shirt','Hoodie','Shirt']:
        raise ValidationError('Clothing type must be one of the following: T-Shirt, Hoodie, Shirt')
    else:
        return value
    
def validate_name(value):
    if value == '':
        raise ValidationError('Name cannot be empty.')
    if not len(value) >= 4:
        raise ValidationError('Name must be at least 4 characters long.')
    if value in BLACKLIST:
        raise ValidationError('Name is not accepted.')
    else:
        return value


