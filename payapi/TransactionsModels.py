from pyexpat import model
from django.db import models

class Transaction(models.Model):
    payment_method = models.CharField(max_length=200)
    credit_card_number = models.CharField(max_length=10,default='--')
    amount = models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    barcode = models.IntegerField()
    payment_date = models.DateField()

    
