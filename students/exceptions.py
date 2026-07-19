from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return Response(
            {
                "success": False,
                "message": "Internal Server Error",
                "errors": {}
            },
            status=500
        )
    messages = {
        status.HTTP_400_BAD_REQUEST:
            "Validation Failed",

        status.HTTP_401_UNAUTHORIZED:
            "Authentication Failed",

        status.HTTP_403_FORBIDDEN:
            "Permission Denied",

        status.HTTP_404_NOT_FOUND:
            "Resource Not Found"
    }
    return Response(
        {
            "success": False,
            "message": messages.get(
                response.status_code,
                "Request Failed"
            ),
            "errors": response.data
        },
        status=response.status_code
    )