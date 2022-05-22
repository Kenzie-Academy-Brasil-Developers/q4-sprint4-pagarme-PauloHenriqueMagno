from rest_framework import serializers

class UserSerializer(serializers.Serializer):
  id = serializers.CharField(read_only = True)
  email = serializers.EmailField()
  password = serializers.CharField(write_only = True)
  first_name = serializers.CharField()
  last_name = serializers.CharField()

  is_admin = serializers.BooleanField(required = False, default = False)
  is_seller = serializers.BooleanField(required = False, default = False)

class LoginUserSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(write_only = True)