# Generated by Django 4.0.6 on 2022-08-14 22:28

from django.db import migrations, models
import gabaystore.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gabaystore', '0004_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[gabaystore.validators.validate_price]),
        ),
    ]