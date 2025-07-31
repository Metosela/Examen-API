from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime
from fastapi.responses import JSONResponse

app = FastAPI()

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

posts_memoire: List[Post] = []

@app.post("/posts", status_code=201)
def create_posts(nouvelle_posts: List[Post]):
    posts_memoire.extend(nouvelle_posts)
    return posts_memoire