from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


from fees.permissions import IsAdmim
from fees.models import Fees
from fees.serializers import FeeSerializer


class FeesView(generics.ListCreateAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated, IsAdmim]

  def post(self, request: Request):
    serializer = FeeSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    fee = Fees.objects.create(**serializer.validated_data)

    serializer = FeeSerializer(fee)

    return Response(serializer.data, 201)

  def get(self, request: Request):
    fees = Fees.objects.all()

    serializer = FeeSerializer(fees, many = True)

    return Response(serializer.data, 200)

class FeesViewId(generics.RetrieveAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAdmim]

  def get(self, request: Request, fee_id):
    fee = Fees.objects.filter(id = fee_id).first()

    if not fee:
      return Response({'message': 'Fee not found'}, 404)

    serializer = FeeSerializer(fee)

    return Response(serializer.data, 200)