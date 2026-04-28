
from flask import Flask,redirect
import base64
#Predefined sets of characters
import string
import random
# To Store the short URL and their associated URLS
url_map={}
nanourl=Flask(__name__)
@nanourl.route('/')
# def home():
#     return "Hello nanoUrl" 
def generate_short_url():
    characters = string.ascii_uppercase+string.ascii_lowercase
    return "".join(random.choices(characters,k=6))
    
    
if __name__=='__main__':
    nanourl.run(debug=True)