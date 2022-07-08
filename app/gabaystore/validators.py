from django.core.exceptions import ValidationError
import os

    
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