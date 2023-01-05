# Generated by Django 4.1.2 on 2022-10-25 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_article_id_alter_comments_id_alter_discount_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['id'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['id'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.article', verbose_name='Статья'),
        ),
        migrations.AddField(
            model_name='comments',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.section', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='article',
            name='datetime',
            field=models.DateTimeField(blank=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.imagegallery', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='datetime',
            field=models.DateTimeField(blank=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product', verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.discount', verbose_name='Скидка'),
        ),
    ]