# Generated by Django 4.2.4 on 2023-08-28 16:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_product_options_alter_stock_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='address',
            field=models.CharField(max_length=200, unique=True, verbose_name='Адрес магазина'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='products',
            field=models.ManyToManyField(related_name='stocks', through='logistic.StockProduct', to='logistic.product', verbose_name='Список продуктов'),
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=18, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='logistic.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='logistic.stock', verbose_name='Склад'),
        ),
    ]
