from fastapi import APIRouter

from scraper import get_wine_data

from schemas import Response, QueryParams


processamento_router = APIRouter(prefix='/processamento')

@processamento_router.get('/viniferas', response_model=Response)
async def get_viniferas_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_03',
        sub_opt='subopt_01'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )

@processamento_router.get('/americanas_e_hibridas', response_model=Response)
async def get_americanas_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_03',
        sub_opt='subopt_02'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )

@processamento_router.get('/uvas_de_mesa', response_model=Response)
async def get_uvas_de_mesa_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_03',
        sub_opt='subopt_03'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )


@processamento_router.get('/sem_classificacao', response_model=Response)
async def get_sem_classificacao_data(year: str):
    query = QueryParams(
        year=year,
        opt='opt_03',
        sub_opt='subopt_04'
    )

    data = await get_wine_data(query)

    return Response(
        message='Success',
        data=data
    )