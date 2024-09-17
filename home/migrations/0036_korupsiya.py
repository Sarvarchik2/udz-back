# Generated by Django 5.1 on 2024-09-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_application_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Korupsiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('pdf_online_link', models.URLField(blank=True, null=True)),
                ('download_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
