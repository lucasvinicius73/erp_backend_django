# Generated by Django 4.1.5 on 2023-03-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='date',
            field=models.DateField(),
        ),
    ]
