# Generated by Django 5.1.1 on 2024-10-09 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('medicin_type', models.CharField(choices=[('kapsul', 'Kapsul'), ('sirup', 'Sirup'), ('tablet', 'Tablet')], default='kapsul', max_length=10)),
                ('medicine_price', models.IntegerField()),
                ('medicine_stock', models.IntegerField()),
            ],
        ),
    ]
