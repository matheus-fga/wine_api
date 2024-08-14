from fastapi import APIRouter

from scraper import get_wine_data

from schemas import Response, QueryParams


importacao_router = APIRouter(prefix='/importacao')

@importacao_router.get('/vinhos_de_mesa', response_model=Response)
async def get_vinhos_de_mesa_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_05',
        sub_opt='subopt_01'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )

@importacao_router.get('/espumantes', response_model=Response)
async def get_espumantes_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_05',
        sub_opt='subopt_02'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )

@importacao_router.get('/uvas_frescas', response_model=Response)
async def get_uvas_frescas_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_05',
        sub_opt='subopt_03'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )

@importacao_router.get('/uvas_passas', response_model=Response)
async def get_uvas_passas_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_05',
        sub_opt='subopt_04'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )

@importacao_router.get('/suco_de_uva', response_model=Response)
async def get_suco_de_uva_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_05',
        sub_opt='subopt_05'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )