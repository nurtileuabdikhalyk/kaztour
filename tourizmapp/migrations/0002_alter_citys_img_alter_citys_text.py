# Generated by Django 4.1.7 on 2023-04-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourizmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citys',
            name='img',
            field=models.CharField(blank=True, max_length=300, verbose_name='Суреті'),
        ),
        migrations.AlterField(
            model_name='citys',
            name='text',
            field=models.CharField(blank=True, max_length=500, verbose_name='Текс'),
        ),
    ]
