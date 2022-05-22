from uuid import uuid4
from django.db import models

class Payable(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
  status = models.CharField(max_length = 50)
  payment_date = models.DateField()
  amount = models.FloatField()

  transaction = models.ForeignKey('transactions.Transactions', on_delete = models.CASCADE)
  fee = models.ForeignKey('fees.Fees', on_delete = models.CASCADE)
  seller = models.ForeignKey('users.Users', on_delete = models.CASCADE)