from django.db import models

# Create your models here.
class User(models.Model):
    class RoleType(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CUSTOMER = 'customer', 'Customer'
        
    username = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(
        max_length=10,
        choices=RoleType.choices,
        default=RoleType.ADMIN
    )
    
    def __str__(self):
        return self.username