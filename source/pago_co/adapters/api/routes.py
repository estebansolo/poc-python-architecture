from fastapi import APIRouter, status, Request, Response
from source.pago_co.prospects.adapters.api.routes import router as prospects_router


router = APIRouter(prefix='/pago_co', tags=["Pago CO"])


router.include_router(prospects_router)