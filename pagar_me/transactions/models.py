from uuid import uuid4
from django.db import models

class Transactions(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
  amount = models.FloatField()
  created_at = models.DateField()
  
  payment_info = models.ForeignKey('paymentInfos.PaymentInfos', on_delete = models.CASCADE)
  seller = models.ForeignKey('users.Users', on_delete = models.CASCADE)