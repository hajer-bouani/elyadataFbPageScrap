import time
time.sleep(2)
import requests
from facebook_scraper import get_posts

posts=get_posts("sami.fehri.tv", pages=1)    
i=0
for post in posts:      
    i+=1
assert(i==2)
print("Scrapper looks fine") 

#r = requests.get("http://127.0.0.1:8000/")
#print("Got response")
#str(r.content)=='b\'{"Hello message":"Welcome to root directory ElyaData"}\''

#print("all good",str(r.content)=='b\'{"Hello message":"Welcome to root directory ElyaData"}\'')

