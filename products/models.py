from uuid import uuid4
from django.db import models

class Products(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
  description = models.CharField(max_length = 255)
  price = models.FloatField()
  quantity = models.IntegerField()

  is_active = models.BooleanField(default = True)

  seller = models.ForeignKey('users.Users', on_delete = models.DO_NOTHING)