from django.db import models

# Create your models here.


class Medicine(models.Model):
    class MedicineType(models.TextChoices):
        KAPSUL = 'kapsul', 'Kapsul'
        SIRUP = 'sirup', 'Sirup'
        TABLET = 'tablet', 'Tablet'
    medicine_name = models.CharField(max_length=100)
    medicin_type = models.CharField(
        max_length=10,
        choices=MedicineType.choices,
        default=MedicineType.KAPSUL
    )
    medicine_price = models.IntegerField()
    medicine_stock= models.IntegerField()
    
    def __str__(self):
        return self.medicine_name
    