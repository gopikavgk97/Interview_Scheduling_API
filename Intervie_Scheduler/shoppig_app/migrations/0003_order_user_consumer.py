# Generated by Django 3.2.12 on 2022-05-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppig_app', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_consumer',
            field=models.CharField(default='Consumer', max_length=200),
            preserve_default=False,
        ),
    ]
