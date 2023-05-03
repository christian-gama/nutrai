from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    This class represents the permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
