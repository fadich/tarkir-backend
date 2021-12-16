from flask import Response

from werkzeug.exceptions import HTTPException


class AuthException(HTTPException):

    def __init__(self, message, code: int = 403):
        super().__init__(
            message,
            Response(
                response=message,
                status=code,
            )
        )
