from rest_framework import permissions


class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user or request.user.is_staff
        return True
