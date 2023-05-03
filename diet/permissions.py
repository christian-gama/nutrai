from rest_framework import permissions


class DietPermission(permissions.BasePermission):
    """
    This class represents the permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        isOwner = obj.user == request.user
        return isOwner
