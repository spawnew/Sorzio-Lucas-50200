# Generated by Django 5.0.1 on 2024-03-04 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0009_alter_singles_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singles',
            name='foto',
            field=models.ImageField(upload_to='media/avatares'),
        ),
    ]
