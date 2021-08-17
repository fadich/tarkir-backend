from flask import Response
from werkzeug.exceptions import HTTPException


class AuthException(HTTPException):

    def __init__(self, message):
        super().__init__(
            message,
            Response(
                'You could not be authenticated. Please refresh the page.', 401,
                {
                    'WWW-Authenticate': 'Basic realm="Login Required"'
                }
            )
        )
