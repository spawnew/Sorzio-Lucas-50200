# Generated by Django 5.0.1 on 2024-03-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0022_alter_singles_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singles',
            name='foto',
            field=models.ImageField(default='../media/avatares/images_4.jpeg', upload_to='media/avatares'),
        ),
    ]
