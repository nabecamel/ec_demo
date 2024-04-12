from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import status

from common.migrations import product
router = APIRouter()

@router.get("/api/products")
async def get_product_list():
    pass