from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def source():
    return {"Hello": "world!"}