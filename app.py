from typing import Optional
from fastapi import FastAPI
app = FastAPI()
from facebook_scraper import get_posts
from pymongo import MongoClient
import requests

#client = MongoClient("mongodb://mongoadmin:secret@0.0.0.0:27017")

@app.get("/")
def read_root():
    client = MongoClient("mongodb://mongoadmin:secret@mongodb")
    db=client.posts
    db.testdbb.insert_one({ "Welcome message": "Welcome to root directory" })
    return {"Hello message": "Welcome to root directory ElyaData"}
    
@app.get("/page/{page_id}")
def read_itemm(page_id: str, q: Optional[int] = 1):
    r = requests.get("https://www.facebook.com/"+page_id)
    client = MongoClient("mongodb://mongoadmin:secret@mongodb")
    db=client.posts
    if str(r)=='<Response [200]>':
        titles=[]
        posts=get_posts(page_id, pages=q)    
        for post in posts:  
            see=db.testdbb.count_documents({'post_id':post['post_id']})
            print(see)
            titles.append(post['text'][:50])
            isthereany=False
            if see==1:
                continue
            else:
                abc=post;abc['pageid']=page_id
                print(abc)
                db.testdbb.insert_one(post)

        return {"You are looking for this page's content": page_id, "Here are the last titles": titles}
    else:
        return {"page_id": "Sorry, but '"+page_id+"' is not a valid facebook page, please make sue that the facebook page is still available and that it is public as the server wasn't able to get a valid response from the facebook page"}




