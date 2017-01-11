from rest_framework import permissions


class ReadOnly(permissions.BasePermission):

    """Only can access non-destructive methods (like GET and HEAD)"""

    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class WriteOnly(permissions.BasePermission):

    """Only can access non-destructive methods (like GET and HEAD)"""

    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in ["POST"]


class AdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.user.is_superuser


class IsOwner(AdminOnly):

    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        view_owner = view.get_view_owner()
        return (request.user == view_owner or
                super(IsOwner, self).has_object_permission(request, view, obj))


class IsOwnerOrReadOnly(ReadOnly):

    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        view_owner = view.get_view_owner()
        # Write permissions are only allowed to the owner of the object.
        return (view_owner == request.user or
                super(IsOwnerOrReadOnly, self).has_object_permission(request, view, obj))


class IsOwnerOrWriteOnly(WriteOnly):

    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        view_owner = view.get_view_owner()
        # Read and Write permissions are only allowed to the owner of the
        # object.
        return (view_owner == request.user or
                super(IsOwnerOrWriteOnly, self).has_object_permission(request, view, obj))
