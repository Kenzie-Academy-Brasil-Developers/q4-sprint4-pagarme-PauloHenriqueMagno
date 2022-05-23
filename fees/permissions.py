from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsAdmim(BasePermission):
  def has_permission(self, request: Request, _):
    allowed_methods = ['GET','POST']

    if request.method in allowed_methods and request.user.is_admin:
      return True

    return False