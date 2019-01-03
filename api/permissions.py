from rest_framework.permissions import BasePermission

class isOwner(BasePermission):
    message = "page only accessible to Staff Members"
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            print (obj.owner)
            return True
        else:
            return False
