# Generated by Django 4.2 on 2023-06-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0010_carousel_sub_title_carousel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to='vendor')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]