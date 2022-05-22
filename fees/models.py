from uuid import uuid4
from django.db import models

class Fees(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
  credit_fee = models.FloatField()
  debit_fee = models.FloatField()
  created_at = models.DateTimeField()