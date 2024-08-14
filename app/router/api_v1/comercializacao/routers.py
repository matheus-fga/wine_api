from fastapi import APIRouter

from scraper import get_wine_data

from schemas import Response, QueryParams


comercializacao_router = APIRouter(prefix='/comercializacao')

@comercializacao_router.get('', response_model=Response)
async def get_comercializacao_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_04'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )