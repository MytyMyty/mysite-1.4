# Generated by Django 5.0.6 on 2024-06-19 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar', models.CharField(max_length=100)),
            ],
        ),
    ]