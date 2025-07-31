from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

posts = [
    {"id": 1, "title": "Premier post", "content": "Ceci est le contenu du premier post"},
    {"id": 2, "title": "Deuxième post", "content": "Voici le deuxième post"}
]

@app.get("/posts")
def get_posts():
    return JSONResponse(content=posts, status_code=200)
