# Generated by Django 3.2.11 on 2022-02-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('p1', models.TextField()),
                ('p2', models.TextField()),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('skills1', models.TextField(max_length=100)),
                ('skill2', models.TextField(max_length=20)),
                ('tools', models.TextField(max_length=30)),
            ],
        ),
    ]
