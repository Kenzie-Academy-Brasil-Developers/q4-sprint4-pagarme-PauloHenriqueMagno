from datetime import datetime
from rest_framework import serializers


class TransactionsSerializer(serializers.Serializer):
  id = serializers.UUIDField(read_only = True)
  amount = serializers.FloatField(read_only = True, required = False)
  created_at = serializers.DateTimeField(read_only = True, required = False)

  seller_id = serializers.UUIDField(read_only = False, format = 'urn')
  seller = seller_id

  payment_info_id = serializers.UUIDField(read_only = False, format = 'urn')
  payment_info = payment_info_id

  def validate(self, data):
    data['created_at'] = datetime.now()
    data['amount'] = 0

    return data