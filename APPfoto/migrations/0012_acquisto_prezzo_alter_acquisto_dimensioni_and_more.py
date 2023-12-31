# Generated by Django 4.2.4 on 2023-09-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPfoto', '0011_rename_created_at_foto_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquisto',
            name='prezzo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='prezzo'),
        ),
        migrations.AlterField(
            model_name='acquisto',
            name='dimensioni',
            field=models.CharField(choices=[('10 x 15   (+0.00)', 0.0), ('12 x 18   (+2.00)', 2.0), ('13 x 19   (+3.00)', 3.0)], max_length=100),
        ),
        migrations.AlterField(
            model_name='acquisto',
            name='materiale',
            field=models.CharField(choices=[('Carta Standard (+0.00)', 0.0), ('Tela (+1.00)', 1.0), ('Carta Fotografica (+2.00)', 2.0), ('Puzzle (+3.50)', 3.5), ('Lamiera Semplice (+3.00)', 3.0), ('Lamiera Premium (+4.00)', 4.0)], max_length=100),
        ),
    ]
