from uuid import uuid4
from django.db import models

class PaymentInfo(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
  payment_method = models.CharField(max_length = 50)
  card_number = models.CharField(max_length = 20)
  cardholders_name = models.CharField(max_length = 150)
  card_expiring_date = models.DateField()
  cvv = models.CharField(max_length = 4)
  
  is_active = models.BooleanField(default = True)

  seller = models.ForeignKey('users.Users', on_delete = models.CASCADE)