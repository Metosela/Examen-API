from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

@app.get("/home", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head><title>Home</title></head>
        <body><h1>Welcome home!</h1></body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request : Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        html_404 = """
        <!DOCTYPE html>
        <html>
            <head><title>404</title></head>
            <body><h1>404 NOT FOUND</h1></body>
        </html>
        """
        return HTMLResponse(content=html_404, status_code=404)
    return HTMLResponse(content=str(exc.detail), status_code=exc.status_code)