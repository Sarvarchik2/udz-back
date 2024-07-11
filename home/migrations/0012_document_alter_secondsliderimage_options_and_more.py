# Generated by Django 5.0.4 on 2024-05-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_delete_mymodel_alter_application_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='documents/')),
            ],
            options={
                'verbose_name': 'Норматив документы',
                'verbose_name_plural': 'Норматив документы',
            },
        ),
        migrations.AlterModelOptions(
            name='secondsliderimage',
            options={'verbose_name': 'Карусель сотрудничество', 'verbose_name_plural': 'Карусель сотрудничество'},
        ),
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'verbose_name': 'Карусель самый верхний', 'verbose_name_plural': 'Карусель самый верхний'},
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='description',
            field=models.TextField(default='Описание'),
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='text',
            field=models.TextField(default='Текст'),
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='title',
            field=models.CharField(default='Заголовок', max_length=200),
        ),
    ]
