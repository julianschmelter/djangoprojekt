from django.db import models

# Create your models here.
class MeinXOEVStandard(models.Model):
    lieferant = models.CharField(max_length=200)
    betrag = models.DecimalField(max_digits=15, decimal_places=2)
    stueckzahl = models.IntegerField()
    
    def __str__(self):
        return f"{self.lieferant} - {self.betrag}€ ({self.stueckzahl} Stück)"