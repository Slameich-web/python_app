from copy import deepcopy

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def typed_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, ValidationError):
            errors = deepcopy(response.data)

            if isinstance(errors, dict):
                custom_errors = {key: list() for key in errors.keys()}
            else:
                return Response({})

            for field, message in errors.items():
                if isinstance(message, dict):
                    custom_errors[field] += message.values()
                elif isinstance(message, list):
                    custom_errors[field] += message
                elif isinstance(message, str):
                    custom_errors[field].append(message)
            response.data = custom_errors

            return Response({
                'errors': custom_errors,
                'code': response.status_code
            }, status=response.status_code, exception=True)

        return Response({
            'message': response.data.get('detail', response.data),
            'code': response.status_code
        }, status=response.status_code, exception=True)

    raise exc
