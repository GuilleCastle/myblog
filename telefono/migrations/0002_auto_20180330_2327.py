# Generated by Django 2.0 on 2018-03-31 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telefono', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='favorito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='telefono.Favoritos'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='telefono.Grupo'),
        ),
    ]