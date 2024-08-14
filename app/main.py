from fastapi import FastAPI

from router.api_v1.producao.routers import producao_router
from router.api_v1.processamento.routers import processamento_router
from router.api_v1.comercializacao.routers import comercializacao_router
from router.api_v1.importacao.routers import importacao_router
from router.api_v1.exportacao.routers import exportacao_router

app = FastAPI()

app.include_router(producao_router, tags=['Produção'])
app.include_router(processamento_router, tags=['Processamento'])
app.include_router(comercializacao_router, tags=['Comercialização'])
app.include_router(importacao_router, tags=['Importação'])
app.include_router(exportacao_router, tags=['Exportação'])
