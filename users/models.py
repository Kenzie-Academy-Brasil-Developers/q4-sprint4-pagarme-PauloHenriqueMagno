from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
  id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
  email = models.CharField(max_length = 150, unique = True, null = False)
  first_name = models.CharField(max_length = 150)
  last_name = models.CharField(max_length = 150)

  is_seller = models.BooleanField(default = False, editable = False)
  is_admin = models.BooleanField(default = False, editable = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []