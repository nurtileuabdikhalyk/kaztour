# Generated by Django 4.1.7 on 2023-04-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourizmapp', '0002_alter_citys_img_alter_citys_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='citys',
            name='descriptions',
            field=models.TextField(blank=True, default='text'),
        ),
    ]
