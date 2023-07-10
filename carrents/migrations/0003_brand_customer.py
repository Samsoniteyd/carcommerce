# Generated by Django 4.2 on 2023-05-15 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('carrents', '0002_rename_text_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
