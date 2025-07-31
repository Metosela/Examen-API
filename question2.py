from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/home", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Welcome home!</h1>
        </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html", status_code=200)