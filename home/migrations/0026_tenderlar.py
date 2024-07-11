# Generated by Django 5.0.4 on 2024-06-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_product_options_product_brand_product_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenderlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.TextField(default='Default Text', verbose_name='Text (English)')),
                ('title_ru', models.TextField(default='Default Text', verbose_name='Text (Russian)')),
                ('title_uz', models.TextField(default='Default Text', verbose_name='Text (Uzbek)')),
                ('text_en', models.TextField(default='Default Text', verbose_name='Text (English)')),
                ('text_ru', models.TextField(default='Default Text', verbose_name='Text (Russian)')),
                ('text_uz', models.TextField(default='Default Text', verbose_name='Text (Uzbek)')),
            ],
            options={
                'verbose_name': 'Tenderlar va konkurslar',
                'verbose_name_plural': 'Tenderlar va konkurslar',
            },
        ),
    ]
