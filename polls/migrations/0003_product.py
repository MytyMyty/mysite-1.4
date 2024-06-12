# Generated by Django 5.0.6 on 2024-06-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_pedido_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('marca', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=35)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('es_publicado', models.BooleanField(default=True)),
                ('fecpub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]