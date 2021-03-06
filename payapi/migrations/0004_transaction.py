# Generated by Django 4.0.5 on 2022-06-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapi', '0003_boleta_importe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=200)),
                ('credit_card_number', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('barcode', models.IntegerField()),
                ('payment_date', models.DateField()),
            ],
        ),
    ]
