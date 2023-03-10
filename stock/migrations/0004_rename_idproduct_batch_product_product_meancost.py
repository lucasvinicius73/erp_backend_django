# Generated by Django 4.1.5 on 2023-03-10 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_batch_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='idProduct',
            new_name='Product',
        ),
        migrations.AddField(
            model_name='product',
            name='meanCost',
            field=models.IntegerField(null=True),
        ),
    ]
