from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_404_NOT_FOUND

from bbfcapi.lib import top_search_result
from bbfcapi.types import Film

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=[],
    allow_credentials=False,
)


@app.get("/", response_model=Film, responses={404: {"model": None}})
async def root(title: str, year: int):
    result = await top_search_result(title, year)
    if result is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Film not found")

    return result


@app.get("/healthz")
async def healthcheck():
    return {"status": "OK"}
