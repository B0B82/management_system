from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.method in permissions.SAFE_METHODS or request.user.is_superuser
