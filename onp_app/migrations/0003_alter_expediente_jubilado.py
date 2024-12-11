# Generated by Django 5.0.4 on 2024-05-29 18:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onp_app', '0002_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='jubilado',
            field=models.ForeignKey(default=1, limit_choices_to={'user_type': 'jubilado'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
