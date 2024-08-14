from fastapi import APIRouter

from scraper import get_wine_data

from schemas import Response, QueryParams


producao_router = APIRouter(prefix='/producao')

@producao_router.get('', response_model=Response)
async def get_producao_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_02'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )