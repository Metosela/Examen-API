from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

posts = []

@app.get("/posts")
def get_posts():
    return posts

@app.put("/posts")
def upsert_post(new_post: Post):
    for post in posts:
        if post["title"] == new_post.title:
            if post["content"] != new_post.content:
                post["content"] = new_post.content
                return {"message": "Post mis à jour"}
            else:
                return {"message": "Aucune modification"}

    posts.append(new_post.dict())
    return {"message": "Post ajouté"}
