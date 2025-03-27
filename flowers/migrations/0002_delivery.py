# Generated by Django 3.2.25 on 2025-03-27 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='адрес')),
                ('delivery_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время доставки')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Выполнена ли доставка')),
                ('buyer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_name_deliveries', to='flowers.buyer', verbose_name='имя покупателя')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
            },
        ),
    ]
