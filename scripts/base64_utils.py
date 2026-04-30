
from flask import Flask,redirect,render_template,request
import base64
#Predefined sets of characters
import string
import random
# To Store the short URL and their associated URLS
url_map={}
nanourl=Flask(__name__,template_folder="../templates")
 
def generate_short_url():
    characters = string.ascii_uppercase+string.ascii_lowercase
    return "".join(random.choices(characters,k=6))
    
@nanourl.route('/',methods=["GET","POST"])
def index():
    shorten_url=None
    if request.method=="POST":
        shorten_url=generate_short_url()
    return render_template("index.html",shorten_url=shorten_url)
if __name__=='__main__':
    nanourl.run(debug=True)