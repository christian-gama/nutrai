from rest_framework import permissions


class PatientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', 'create']:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve', 'create']:
            return True

        isAuthenticated = request.user and request.user.is_authenticated
        isOwner = obj.user == request.user

        return isAuthenticated and isOwner
