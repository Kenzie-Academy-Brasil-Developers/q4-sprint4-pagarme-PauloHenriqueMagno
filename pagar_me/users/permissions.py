from rest_framework.permissions import BasePermission
        
class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        
        if request.method == 'GET':
            if (request.user.is_authenticated and request.user.is_admin == True):
                return True

        return False