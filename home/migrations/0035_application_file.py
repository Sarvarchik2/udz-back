# Generated by Django 5.1 on 2024-08-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_alter_application_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='applications/'),
        ),
    ]
