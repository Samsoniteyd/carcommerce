# Generated by Django 4.2 on 2023-04-24 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('stores', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('subtotal', models.PositiveIntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.product')),
            ],
        ),
    ]
