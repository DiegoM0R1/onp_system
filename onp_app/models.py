from django.db import models
from django.contrib.auth.models import AbstractUser

  


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USER_TYPE_CHOICES = [
        ('trabajador', 'Trabajador ONP'),
        ('jubilado', 'Jubilado'),
        ('administrador', 'Administrador'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='jubilado')
   
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Cambia este nombre a algo que no esté en conflicto
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Cambia este nombre a algo que no esté en conflicto
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Expediente(models.Model):
    jubilado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'jubilado'}, default=1) # Cambia el valor predeterminado según el ID del usuario jubilado predeterminado
    identificador_unico = models.CharField(max_length=100, unique=True)
    datos_jubilado = models.TextField()
    historial_aportes = models.TextField(null=True, blank=True)
    calculo_pension = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado_expediente = models.CharField(max_length=100, default='Pendiente')


