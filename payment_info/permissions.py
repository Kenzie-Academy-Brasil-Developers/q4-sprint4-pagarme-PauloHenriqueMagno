from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class IsBuyer(BasePermission):
  def has_permission(self, request: Request, _):
    allowed_methods = ['GET','POST']

    if request.method in allowed_methods and (
      not request.user.is_anonymous
      and not request.user.is_admin
      and not request.user.is_seller
    ):
      return True

    return False