from django.core.exceptions import ValidationError
from django import forms
import os

def validate_file_type(value):
    filetype = value.content_type
    if not filetype in ['image/jpeg', 'image/png']:
        raise ValidationError(u'Unsupported file type.')
    
def validate_file_name(value):
    filename = value.name
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise ValidationError(u'Unsupported file extension.')

def validate_file_extension_and_size(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
    filesize = value.size
    if filesize > 2097152:
        raise ValidationError(u'File too large. Size limit is 2 MB.')

def validate_price(value):
    if value < 0:
        raise ValidationError(u'Price cannot be negative.')
    if value == 0:
        raise ValidationError(u'Price cannot be zero.')
    
def validate_quantity(value):
    if value < 0:
        raise ValidationError(u'Quantity cannot be negative.')
    if value == 0:
        raise ValidationError(u'Quantity cannot be zero.')