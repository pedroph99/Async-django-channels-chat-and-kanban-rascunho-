# Generated by Django 4.1 on 2022-10-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_alter_usuarios_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
