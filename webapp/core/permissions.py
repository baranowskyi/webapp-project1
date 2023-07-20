from rest_framework import permissions

# if owner or admin
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):        
        if request.user.is_staff:
            return True
        return obj.user == request.user
    
    
# if owner or read only
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
    
# readonly    
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS