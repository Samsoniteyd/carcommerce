# Generated by Django 4.2 on 2023-06-15 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0012_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='Date',
            new_name='created',
        ),
    ]
