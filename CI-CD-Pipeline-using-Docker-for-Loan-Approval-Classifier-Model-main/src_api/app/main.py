import sys
import logging
from pathlib import Path
from typing import Any

import uvicorn
from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Setup path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Import local modules
from app.api import api_router
from app.config import settings
from app.middleware.error_handler import (
    error_handler,
    rate_limit_exceeded_handler,
    validation_error_handler,
    LoanApprovalException
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="Loan Approval Classifier API with automated predictions",
    version="1.0.0",
)

# Add error handlers
app.add_exception_handler(LoanApprovalException, error_handler)
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)
app.add_exception_handler(Exception, error_handler)

# Root router
root_router = APIRouter()

@root_router.get("/")
@limiter.limit("10/minute")
def index(request: Request) -> Any:
    """Welcome page with API documentation link."""
    body = (
        "<html>"
        "<body style='padding: 20px; font-family: Arial, sans-serif;'>"
        "<h1>Welcome to the Loan Approval Classifier API</h1>"
        "<div style='margin-top: 20px;'>"
        "<p>This API provides loan approval predictions based on machine learning models.</p>"
        "<p>Check the API documentation: <a href='/docs'>here</a></p>"
        "</div>"
        "</body>"
        "</html>"
    )
    return HTMLResponse(content=body)

# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
)

# Add trusted host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1"]
)

@app.on_event("startup")
async def startup_event():
    """Perform startup tasks."""
    logger.info("Starting up the application...")

@app.on_event("shutdown")
async def shutdown_event():
    """Perform cleanup on shutdown."""
    logger.info("Shutting down the application...")
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 

    ## local host--> 127.0.0.0  
    ## host --> 0.0.0.0 allows all host
