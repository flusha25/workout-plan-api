from rest_framework import permissions

class ReadOnlyPermission(permissions.BasePermission):
    """
    Custom permission to allow only GET requests.
    """

    def has_permission(self, request, view):
        return request.method == 'GET'