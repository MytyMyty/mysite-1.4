# Generated by Django 5.0.6 on 2024-06-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_product_preciod_alter_product_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='preciod',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
