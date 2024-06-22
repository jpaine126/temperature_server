from rest_framework.permissions import BasePermission

from . import settings


class SafelistPermission(BasePermission):
    """
    Ensure the request's IP address is on the safe list configured in Django settings.
    """

    message = "Not on IP whitelist"

    def has_permission(self, request, view):

        remote_addr = request.META["REMOTE_ADDR"]

        for valid_ip in settings.REST_SAFE_LIST_IPS:
            if remote_addr == valid_ip or remote_addr.startswith(valid_ip):
                return True

        return False
