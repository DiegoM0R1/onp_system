# Generated by Django 5.0.4 on 2024-05-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('trabajador', 'Trabajador ONP'), ('jubilado', 'Jubilado'), ('administrador', 'Administrador')], default='jubilado', max_length=20),
        ),
    ]
