from rest_framework import viewsets,permissions


class IsSafeMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)
class IsPurchase(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool( view.action in ('purchase', 'purchase_items'))