# Generated by Django 5.0.1 on 2024-03-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0032_alter_producto_fproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fproducto',
            field=models.ImageField(default='avatares/default_1.jpeg', upload_to='media'),
        ),
    ]
