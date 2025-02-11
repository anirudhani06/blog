from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    def as_object_permissions(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author==request.user
        
        