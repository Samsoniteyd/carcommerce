# Generated by Django 4.2 on 2023-06-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_remove_order_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='sub_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
