from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from products.serializers import (
  ProductSerializer,
  ProductPatchSerializer,
  ProductSellerSerializer
)
from products.permissions import IsSeller
from products.models import Products

from users.models import Users

class ProductView(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsSeller]

  def post(self, request: Request):
    user: Users = request.user

    serialiser = ProductSerializer(data=request.data)
    serialiser.is_valid(raise_exception = True)

    serialiser.validated_data['seller'] = user
    product = Products.objects.create(**serialiser.validated_data)

    serialiser = ProductSellerSerializer(product)

    serialiser.data['seller'] = user.id

    return Response(serialiser.data, 201)

  def get(self, _: Request):
    serialiser = ProductSerializer(
      Products.objects.filter(is_active = True), many = True
    )

    return Response(serialiser.data, 200)


class ProductGetPatchView(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsSeller]

  def get(self, _: Request, product_id):
    products = Products.objects.filter(id = product_id)

    if not products.first():
      return Response({'message': 'Products not found'}, 404)

    serialiser = ProductSerializer(products.first())

    return Response(serialiser.data, 200)

  def patch(self, request: Request, product_id):
    user: Users = request.user

    product = Products.objects.filter(id = product_id).first()

    if not product:
      return Response({'message': 'Product not found'}, 404)

    if product.seller.id != user.id:
      return Response({'detail': 'You do not have permission to perform this action.'}, 401)

    serializer = ProductPatchSerializer(request.data)

    Products.objects.filter(id = product_id).update(**serializer.data)

    product = Products.objects.filter(id = product_id).first()

    serializer = ProductPatchSerializer(product)

    return Response(serializer.data, 200)

class ProductsBySellerId(APIView):
  def get(self, _: Request, seller_id):
    seller: Users = Users.objects.filter(id=seller_id).first()
    
    if not seller:
      return Response({'detail': 'Not found.'}, 404)

    serialiser = ProductSerializer(
      Products.objects.filter(seller = seller_id), many = True
    )

    return Response(serialiser.data, 200)
