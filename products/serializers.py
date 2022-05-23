from rest_framework import serializers

from users.serializers import UserSerializer

class ProductSerializer(serializers.Serializer):
  id = serializers.CharField(read_only = True)
  description = serializers.CharField()
  price = serializers.FloatField(min_value = 0)
  quantity = serializers.IntegerField(min_value = 0)

  is_active = serializers.BooleanField(required = False, default = True)

  seller_id = serializers.CharField(read_only = True)
  seller = seller_id

class ProductSellerSerializer(ProductSerializer):
  seller = UserSerializer(read_only = True)

class ProductPatchSerializer(ProductSerializer):
  description = serializers.CharField(required = False)
  price = serializers.FloatField(required = False, min_value = 0)
  quantity = serializers.IntegerField(required = False, min_value = 0)

  is_active = serializers.BooleanField(required = False)