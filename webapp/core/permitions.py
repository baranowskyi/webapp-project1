from rest_framework.permissions import BasePermission

# if owner or admin
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):        
        if request.user.is_staff:
            return True
        return obj.user == request.user