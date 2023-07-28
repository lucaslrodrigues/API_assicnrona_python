from fastapi import APIRouter
import sys
# sys.path.insert(1, '../app')
from app.utils.generate_token import Token

router = APIRouter()

@router.get("/")
async def source():
    return {"Hello": "world!"}

@router.get("/token/{token_acess}")
async def send_token():
    gerador_token = Token()
    gerador_token.generate_token()
    return {"token_value": "%d" % (gerador_token.get_token())}