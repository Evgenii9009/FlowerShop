# Generated by Django 4.2 on 2025-03-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0006_alter_consult_options_remove_consult_buyer_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consult',
            options={'verbose_name': 'Консультация', 'verbose_name_plural': 'Консультации'},
        ),
        migrations.AddField(
            model_name='consult',
            name='consult_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата и время запроса консультации'),
        ),
    ]
