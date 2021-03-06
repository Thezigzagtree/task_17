from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "page only accessible to Staff Members"
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user or request.user.is_staff:
            return True
        else:
            return False
