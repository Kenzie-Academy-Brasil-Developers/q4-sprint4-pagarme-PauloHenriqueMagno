from unittest import result
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.request import Request
from rest_framework.response import Response


from payables.permissions import IsSeller
from payables.models import Payable
from payables.serializer import PayablesSerializer

class PayablesView(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsSeller]

  def get(self, request: Request):
    payables = Payable.objects.filter(seller_id = request.user.id)

    paid = sum([payable for payable in payables if payable.status == "paid"])
      
    payables = [payable for payable in payables if payable.status == "waiting_funds"]

    serializer = PayablesSerializer(payables, many = True)

    waiting_funds = 0

    for payable in serializer.data:
      payable_dict = dict(payable)
      waiting_funds += -float(payable_dict['amount'])

    result = {
      "payable_amount_paid": paid,
      "payable_amount_waiting_funds": float('{:.2f}'.format(waiting_funds)),
    }

    return Response(result, 200)