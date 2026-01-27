from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AppException
from app.schemas.response import APIResponse, ErrorResponse


def app_exception_handler(request: Request, exc: AppException):
    response = APIResponse(
        success=False,
        data=None,
        error=ErrorResponse(
            message=exc.message,
            code=exc.code
        )
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump()
    )