from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(tags=["API Health Checker"])


@router.get(
    path="/",
    response_class=JSONResponse,
    name="api-health:check-health",
    status_code=status.HTTP_200_OK,
)
async def check_health() -> JSONResponse:
    return JSONResponse(content={"status": "💚"})
