from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class IsCostumerAdm(BasePermission):
    def has_permission(self, request: Request, _):

        if request.user.is_anonymous:
            return False

        if (
            request.method == "POST"
            and not request.user.is_admin
            and not request.user.is_seller
        ):
            return True

        if request.method == "GET" and request.user.is_admin or request.user.is_seller:
            return True

        return False
