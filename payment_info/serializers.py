from rest_framework import serializers

class PaymentInfoSerializer(serializers.Serializer):
  id = serializers.CharField(read_only = True)
  payment_method = serializers.CharField()
  card_number = serializers.CharField(max_length = 19, min_length = 13)
  cardholders_name = serializers.CharField()
  card_expiring_date = serializers.DateField(format = '%Y-%m-%d', input_formats=['%Y-%m-%d'])
  cvv = serializers.CharField(max_length = 4)

  is_active = serializers.BooleanField(required = False)

  customer_id = serializers.CharField(read_only = True, required = False)
  customer = customer_id