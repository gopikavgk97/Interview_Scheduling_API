# Generated by Django 3.2.12 on 2022-05-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppig_app', '0003_order_user_consumer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.FloatField()),
                ('product_quantity', models.PositiveIntegerField()),
            ],
        ),
    ]