# Generated by Django 4.2 on 2023-04-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourizmapp', '0009_citys_descriptions_1_alter_citys_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='citys',
            name='img_1',
            field=models.CharField(blank=True, default='text', max_length=300, verbose_name='Суреті_1'),
        ),
        migrations.AlterField(
            model_name='citys',
            name='img',
            field=models.CharField(blank=True, max_length=300, verbose_name='Суреті'),
        ),
    ]
