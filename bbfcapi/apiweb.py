from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

from bbfcapi.apilib import top_search_result
from bbfcapi.types import Film

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=[],
    allow_credentials=False,
)


@app.get("/", response_model=Film)
async def root(title: str, year: int):
    result = await top_search_result(title, year)
    if result is None:
        return Response(status_code=HTTP_204_NO_CONTENT)

    return result


@app.get("/healthz")
async def healthcheck():
    return {"status": "OK"}
