# Generated by Django 4.2.4 on 2023-09-07 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('APPfoto', '0009_alter_foto_actual_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
