from aiohttp import ClientSession
from bs4 import BeautifulSoup
from fastapi import HTTPException
from fastapi import status as http_status

from schemas import Value, Item, WineData, QueryParams

BASE_WINE_DATA_URL = 'http://vitibrasil.cnpuv.embrapa.br/index.php'

async def get_html_from_url(url):
    
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            text = await response.text()

            if response.status == 200:
                html = BeautifulSoup(markup=text, features="html.parser")

                return html

    raise HTTPException(status_code=http_status.HTTP_503_SERVICE_UNAVAILABLE,
                        detail=f"Scraper didn't succeed in getting data:\n"
                               f"\turl: {url}\n"
                               f"\tstatus code: {response.status}\n"
                               f"\tresponse text: {text}")


def parse_wine_data(html: BeautifulSoup):
    wine_data_description = html.select_one('.text_center').text[:-7].strip()
    wine_data_year = html.select_one('.text_center').text.strip()[-5:-1]
    value1_description = html.select_one('.tb_base.tb_dados thead tr th:nth-child(2)').text.strip()
    value2_description = html.select_one('.tb_base.tb_dados thead tr th:nth-child(3)')
    itens = []
    values = []

    for item in html.select('.tb_base.tb_dados tbody tr'):
        name = item.select_one('td:nth-child(1)')
        value1 = item.select_one('td:nth-child(2)')
        value2 = item.select_one('td:nth-child(3)')
        
        if not value2:
            values = [
                Value(unit=value1_description, value=value1.text.strip())
            ]
        else:
            values = [
                Value(unit=value1_description, value=value1.text.strip()),
                Value(unit=value2_description.text.strip(), value=value2.text.strip())
            ]
        
        itens.append(
            Item(
                name=name.text.strip(),
                values=values
            )
        )

    return WineData(
        description=wine_data_description,
        year=wine_data_year,
        data=itens
    )

    
async def get_wine_data(query: QueryParams):
    if not query.sub_opt:
        url = f'{BASE_WINE_DATA_URL}?ano={query.year}&opcao={query.opt}'
    else:
        url = f'{BASE_WINE_DATA_URL}?ano={query.year}&opcao={query.opt}&subopcao={query.sub_opt}'

    page = await get_html_from_url(url)

    wine_data = parse_wine_data(page)

    return wine_data

