# Generated by Django 4.1.2 on 2022-11-09 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_slug_section_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.DeleteModel(
            name='ImageGallery',
        ),
    ]
