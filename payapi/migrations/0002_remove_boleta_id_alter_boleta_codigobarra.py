# Generated by Django 4.0.5 on 2022-06-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleta',
            name='id',
        ),
        migrations.AlterField(
            model_name='boleta',
            name='codigoBarra',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
