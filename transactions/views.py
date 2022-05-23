from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from datetime import timedelta

from fees.models import Fees

from users.models import Users

from payables.models import Payable
from payables.serializer import PayablesSerializer

from products.models import Products

from payment_info.models import PaymentInfo
from payment_info.utils import is_card_expired

from orders.models import Orders

from transactions.models import Transactions
from transactions.permissions import IsCostumerAdm
from transactions.serializers import TransactionsSerializer

class TransactionsView(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsCostumerAdm]

  def post(self, request: Request):
    seller = request.data['seller']
    products = request.data['seller']['products']
    payment_info = request.data['payment_info']

    payment_card: PaymentInfo = PaymentInfo.objects.filter(id = payment_info['id']).first()

    if not payment_card:
      return Response({'error': ['Card not found']}, 400)

    if not is_card_expired(payment_card.card_expiring_date):
      return Response({'error': ['This card is expired']}, 400)
  
    if payment_card.customer.id != request.user.id:
      return Response({'error': ['Card not found']}, 400)

    seller = Users.objects.filter(id = seller['id']).first()

    if not seller:
      return Response({'error': ['All products must belong to the same seller']}, 400)
    
    data = {'payment_info': payment_card.id, 'seller': seller.id}
    
    serializer = TransactionsSerializer(data = data)
    serializer.is_valid(raise_exception = True)

    transactions = Transactions.objects.create(**serializer.validated_data)

    total = 0

    for product in products:
        seller_product = Products.objects.filter(id = product['id']).first()
        
        if not seller_product:
          return Response({'error': ['Product not found']}, 400)

        if seller_product.quantity < product['quantity']:
          return Response({'error': ['The product quantity is lower']}, 400)

        if not seller_product.is_active:
          return Response({'error': ['Product is not active']}, 400)

        amount = seller_product.price * product['quantity']

        Orders.objects.create(
          product = seller_product,
          quantity = product['quantity'],
          amount = amount,
          transaction = transactions
        )

        seller_product.quantity -= product['quantity']
        seller_product.save()

        total += amount

    transactions.amount = total
    transactions.save()

    fee: Fees = Fees.objects.last()

    if payment_card.payment_method == 'credit':
      payable_obj = {
        'status': 'waiting_funds',
        'payment_date': transactions.created_at + timedelta(days = 30),
        'amount': transactions.amount - float(fee.credit_fee) * 100,
      }

    if payment_card.payment_method == 'debit':
      payable_obj = {
        'status': 'paid',
        'payment_date': transactions.created_at,
        'amount': transactions.amount - float(fee.debit_fee) * 100,
      }

    payable = Payable.objects.create(
      **payable_obj,
      transaction = transactions,
      fee = fee,
      seller = seller
    )

    serializer = PayablesSerializer(payable)

    return Response(serializer.data, 200)

  def get(self, request: Request):
    payables = Payable.objects.all()

    if request.user.is_seller:
      payables = payables.filter(seller_id=request.user.id).all()
    serializer = PayablesSerializer(payables, many = True)

    return Response(serializer.data, 200)
