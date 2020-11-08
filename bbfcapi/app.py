from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_404_NOT_FOUND

from bbfcapi.lib_async import best_match
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
async def root(title: str):
    result = await best_match(title)
    if result is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Film not found")

    return result


@app.get("/healthz")
async def healthcheck():
    return {"status": "OK"}
