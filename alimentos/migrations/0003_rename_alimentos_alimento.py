# Generated by Django 4.2.8 on 2024-07-20 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0002_alimentos_disponibilidade'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alimentos',
            new_name='Alimento',
        ),
    ]
