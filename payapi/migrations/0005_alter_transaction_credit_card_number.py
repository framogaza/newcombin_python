# Generated by Django 4.0.5 on 2022-06-16 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapi', '0004_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='credit_card_number',
            field=models.CharField(default='--', max_length=10),
        ),
    ]
