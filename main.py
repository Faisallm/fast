from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

# the name of the function never matters

app = FastAPI()

# we need to define how  our model should look like
# 
class Post(BaseModel):
    title: str
    content: str
    # giving a field a default value
    published: bool = True
    # optional field, if not provided
    # give it a default value of None
    rating: Optional[int] = None


@app.get("/")
def root():
    return {'message': "Welcome to faisal's api"}

@app.get('/posts')
def get_posts():
    return {"data": "These are your posts"}

# extract all the data from the body.
# store in a python dictionary (since its json in the body)
# store in a variable called payload

# pydantic will validate the data for us.
@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.published)
    # store it to db  or something
    # return some validation
    return  {"data":  f"new_post"}
    


