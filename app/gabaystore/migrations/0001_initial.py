# Generated by Django 3.2.13 on 2022-06-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('picture', models.ImageField(upload_to='')),
                ('size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
                ('clothing_type', models.CharField(choices=[('T-Shirt', 'T-Shirt'), ('Hoodie', 'Hoodie'), ('Shirt', 'Shirt')], max_length=20)),
            ],
            options={
                'db_table': 'Cloth',
            },
        ),
    ]