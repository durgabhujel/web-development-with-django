# Generated by Django 3.2.11 on 2022-02-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_image2',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
