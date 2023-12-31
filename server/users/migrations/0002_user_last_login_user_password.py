# Generated by Django 4.2.4 on 2023-08-24 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
