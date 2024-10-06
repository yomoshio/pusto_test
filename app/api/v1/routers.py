"""
API Routers Initialization.

This module initializes the API routers by including each of the
individual routers (articles, comments, and users) into the main API router.

"""

from fastapi import APIRouter


from app.api.v1.prize.routes import router as prize_router

# Initialize the main API router for version 1.
main_api_router = APIRouter()

# List of individual routers to be included in the main API router.
api_routers = [prize_router]

# Include each router from the list into the main API router.
for api_router in api_routers:

    main_api_router.include_router(api_router)
