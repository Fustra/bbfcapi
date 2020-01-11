from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from bbfcapi.client import search
from bbfcapi.parser import top_search_result
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
    # TODO: Handle no films found for that year
    # TODO: Year optional?
    page = await search(title, year)
    return top_search_result(page)


@app.get("/healthz")
async def healthcheck():
    return {"status": "OK"}
