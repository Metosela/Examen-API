from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)