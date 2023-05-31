from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()

@app.get('/teste')
async def teste(settings: Settings = Depends(get_settings)):
    return {
        "response": "ok 200",
        "enviroment": settings.enviroment,
        "testing": settings.testing
    }