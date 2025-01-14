# Generated by Django 5.0.6 on 2024-06-15 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_delete_users_remove_registro_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comidas',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.registro'),
        ),
        migrations.AlterField(
            model_name='postres',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.registro'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
