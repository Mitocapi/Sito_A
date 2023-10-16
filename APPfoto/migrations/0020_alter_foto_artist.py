# Generated by Django 4.2.4 on 2023-09-11 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APPfoto', '0019_alter_recensione_voto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='artist',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto', to=settings.AUTH_USER_MODEL),
        ),
    ]