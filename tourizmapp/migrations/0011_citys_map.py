# Generated by Django 4.2 on 2023-04-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourizmapp', '0010_citys_img_1_alter_citys_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='citys',
            name='map',
            field=models.CharField(blank=True, default='text', max_length=500, verbose_name='Карта'),
        ),
    ]