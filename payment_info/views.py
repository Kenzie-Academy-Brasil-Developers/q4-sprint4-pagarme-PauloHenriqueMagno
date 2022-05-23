from rest_framework.authentication import TokenAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from payment_info.models import PaymentInfo
from payment_info.serializers import PaymentInfoSerializer
from payment_info.permissions import IsBuyer
from payment_info.utils import format_card_number, is_card_expired

from users.models import Users

class PaymentesInfoView(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsBuyer]

  def post(self, request: Request):
    user: Users = request.user

    serializer = PaymentInfoSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    if not is_card_expired(request.data.get('card_expiring_date')):
      return Response({'error': ['This card is expired']}, 400)

    card = PaymentInfo.objects.filter(
      card_number = serializer.validated_data['card_number'],
      payment_method = serializer.validated_data['payment_method']
    ).first()

    if card:
      return Response({'error': ['This card is already registered for this user']}, 422)

    serializer.validated_data['customer'] = user
    paymentInfo: PaymentInfo = PaymentInfo.objects.create(**serializer.validated_data)

    serializer = PaymentInfoSerializer(paymentInfo)

    return Response(serializer.data, 201)

  def get(self, request: Request):
    user: Users = request.user
    serializer = PaymentInfoSerializer(
      PaymentInfo.objects.filter(customer_id=user.id).all(), many=True
    )
    response = []
    for payment in serializer.data:
      paymentInfo = dict(payment).copy()
      paymentInfo['card_number'] = format_card_number(paymentInfo['card_number'])
      paymentInfo['customer'] = user.id

      response.append(paymentInfo)

    return Response(response, 200)
