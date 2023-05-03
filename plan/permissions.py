from rest_framework import permissions

from plan.models import Plan


class PlanPermission(permissions.BasePermission):
    """
    This class represents the permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj: Plan):
        isOwner = obj.diet.user == request.user
        return isOwner
