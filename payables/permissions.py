from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class IsSeller(BasePermission):
  def has_permission(self, request: Request, _):
    allowed_methods = ["GET"]
    
    if request.method in allowed_methods and (
      request.user.is_anonymous or not request.user.is_seller
    ):
      return False

    return True