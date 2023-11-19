from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

# the name of the function never matters

app = FastAPI()

my_posts = [
    {
        'title': "LLM's  Large Language Models", 
        "content": "Attention is all you need", 
        "published": "false", 
        "rating": "3",
        "id": 1 
        },
    {
        'title': "Deep Learning", 
        "content": "The cool kid getting all the attention.", 
        "published": "true", 
        "rating": "1",
        "id": 2 
        }]

# we need to define how  our model should look like
# 

def find_post(id):
    post = [post for post in my_posts if post['id'] == id]
    if len(post) > 0:
        return post[0]
    return None

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
    return {"data": my_posts}

# extract all the data from the body.
# store in a python dictionary (since its json in the body)
# store in a variable called payload

# pydantic will validate the data for us.
@app.post("/posts")
def create_posts(post: Post):
    rand_int = randrange(0, 10000000)
    # convert the pydantic post schema...
    # into a dictionary
    new_post = post.dict()
    new_post['id'] = rand_int
    # store it to db  or something
    my_posts.append(new_post)
    # return some validation
    return  {"data":  new_post}
    
# this is a path parameter
# anytime we have a path parameter its 
# going to be returned as a string.
@app.get("/posts/{id}")
def get_post(id: int):
    print(type(id))
    post = find_post(id)
    print(post)
    return  {"post_detail": post}
    

