from sqlite3 import IntegrityError

from django.contrib.auth import authenticate

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from users.permissions import UserPermissions
from users.models import Users

from users.serializers import UserSerializer

class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermissions]

    def post(self, request: Request):
        try:
            serializer = UserSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)

            isEmailTaken = Users.objects.filter(
                email = serializer.validated_data["email"]
            ).exists()

            if isEmailTaken:
                return Response({"message": "User already exists"}, 422)

            newUser = Users.objects.create(**serializer.validated_data)

            newUser.set_password(serializer.validated_data['password'])

            if newUser.is_admin:
                newUser.is_seller = False

            newUser.save()

            userSerialized = UserSerializer(newUser)

            return Response( userSerialized.data, 201 )

        except IntegrityError as error:
            return Response(str(error), 400)

