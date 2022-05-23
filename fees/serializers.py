from email.policy import default
from rest_framework import serializers
from datetime import datetime

class FeeSerializer(serializers.Serializer):
  id = serializers.CharField(read_only = True)
  credit_fee = serializers.FloatField(min_value = 0)
  debit_fee = serializers.FloatField(min_value = 0)
  created_at = serializers.DateTimeField(required = False)

  def validate(self, data):
    data['created_at'] = datetime.now()

    return data