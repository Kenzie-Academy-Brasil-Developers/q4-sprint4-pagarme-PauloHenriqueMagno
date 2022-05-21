from uuid import uuid4
from django.db import models

class Orders(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
  quantity = models.IntegerField()
  amount = models.IntegerField()

  transaction = models.ForeignKey('transactions.Transactions', on_delete = models.CASCADE)
  product = models.ForeignKey('products.Products', on_delete = models.CASCADE)