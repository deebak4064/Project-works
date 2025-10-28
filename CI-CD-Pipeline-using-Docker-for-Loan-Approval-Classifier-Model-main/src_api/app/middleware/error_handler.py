from fastapi import Request, status
from fastapi.responses import JSONResponse
from typing import Union
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LoanApprovalException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

async def error_handler(request: Request, exc: Union[Exception, LoanApprovalException]) -> JSONResponse:
    """Global error handler for the application."""
    if isinstance(exc, LoanApprovalException):
        logger.error(f"LoanApprovalException: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.message}
        )
    
    # Handle other exceptions
    logger.error(f"Unexpected error: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal server error"}
    )

# Rate limiting error handler
async def rate_limit_exceeded_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handler for rate limiting exceptions."""
    logger.warning(f"Rate limit exceeded for IP: {request.client.host}")
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={"error": "Too many requests. Please try again later."}
    )

# Validation error handler
async def validation_error_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handler for request validation errors."""
    logger.error(f"Validation error: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"error": "Invalid request data", "details": str(exc)}
    )