class AppException(Exception):
    def __init__(self, message: str, code: str, status_code: int):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(message)


class NotFoundException(AppException):
    def __init__(self, message: str = 'Resource not found'):
        super().__init__(
            message=message,
            code='NOT_FOUND',
            status_code=404
        )


class BadRequestExeption(AppException):
    def __init__(self, message: str = 'Bad request'):
        super().__init__(
            message=message,
            code='BAD_REQUEST',
            status_code=400
        )
