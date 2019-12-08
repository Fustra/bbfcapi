from fastapi import FastAPI

from bbfcapi.client import search
from bbfcapi.parser import top_search_result
from bbfcapi.types import Film

app = FastAPI()


@app.get("/", response_model=Film)
async def root(title: str, year: int):
    page = await search(title, year)
    return top_search_result(page)


@app.get("/healthz")
async def healthcheck():
    return {"status": "OK"}
