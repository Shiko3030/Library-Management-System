# Generated by Django 5.0.6 on 2024-09-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0015_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
