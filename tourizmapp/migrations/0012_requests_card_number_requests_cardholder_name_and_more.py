# Generated by Django 4.2 on 2023-04-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourizmapp', '0011_citys_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='card_number',
            field=models.CharField(blank=True, default='456789654321', max_length=100, verbose_name='Карта номері'),
        ),
        migrations.AddField(
            model_name='requests',
            name='cardholder_name',
            field=models.CharField(blank=True, default='Admin test', max_length=100, verbose_name='Карта иесі'),
        ),
        migrations.AddField(
            model_name='requests',
            name='cvc',
            field=models.CharField(blank=True, default='456', max_length=100, verbose_name='CVC код'),
        ),
        migrations.AddField(
            model_name='requests',
            name='expiration_date',
            field=models.CharField(blank=True, default='12/24', max_length=100, verbose_name='Жарамдылық мерзімі'),
        ),
    ]
