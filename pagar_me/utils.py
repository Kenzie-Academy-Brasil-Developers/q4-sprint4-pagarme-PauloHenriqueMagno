from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import PermissionDenied

def permission_denied_handler(exc: Exception, context):
  response = exception_handler(exc, context)

  if isinstance(exc, PermissionDenied):
    if 'not have permission' in str(exc):
      return Response({'detail': 'You do not have permission to perform this action.'}, 403)

  return response