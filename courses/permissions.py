from rest_framework import permissions

# This method allows only the admin to perform CRUD operations.
# All other users can only read
class IsStaffOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)