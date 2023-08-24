# Generated by Django 4.2.4 on 2023-08-24 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calculation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата подсчета')),
                ('total', models.FloatField(verbose_name='Итог')),
                ('product_count', models.IntegerField(verbose_name='Количество продаж')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Доход',
                'verbose_name_plural': 'Доходы',
            },
        ),
    ]
